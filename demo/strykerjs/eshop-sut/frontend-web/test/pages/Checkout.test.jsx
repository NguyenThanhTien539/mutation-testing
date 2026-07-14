import { useState } from 'react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent, waitFor, act } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import axios from 'axios';
import { AuthProvider, useAuth } from '../../src/context/AuthContext';
import { CartProvider, useCart } from '../../src/context/CartContext';
import Checkout from '../../src/pages/Checkout';

vi.mock('axios', () => ({
  default: {
    get: vi.fn(() => Promise.resolve({ data: {} })),
    post: vi.fn(() => Promise.resolve({ data: {} })),
    defaults: { headers: { common: {} } },
  },
}));

const PRODUCT = { id: 1, name: 'Áo Thun', price: 100000 };
const LOGIN_RESPONSE = {
  token: 'jwt-token-abc',
  user: { id: 7, name: 'Nguyen Van A', role: 'customer' },
};

/**
 * Exposes the real AuthContext/CartContext handles for the test to drive
 * function A (login/addToCart) before exercising function B (Checkout),
 * inside the same provider tree so state genuinely flows between them.
 * Checkout only mounts once `revealCheckout` is called, so a test can seed
 * login/cart state *before* Checkout's own `useState(cartTotal)` captures
 * its initial value - mirroring how a real user logs in and adds items on
 * other pages before ever navigating to /checkout.
 */
function Harness({ apiRef, initiallyVisible }) {
  const [visible, setVisible] = useState(initiallyVisible);
  apiRef.current = { auth: useAuth(), cart: useCart(), revealCheckout: () => setVisible(true) };
  return visible ? <Checkout /> : null;
}

function renderApp({ showCheckout = true } = {}) {
  const apiRef = { current: null };
  const utils = render(
    <MemoryRouter>
      <AuthProvider>
        <CartProvider>
          <Harness apiRef={apiRef} initiallyVisible={showCheckout} />
        </CartProvider>
      </AuthProvider>
    </MemoryRouter>,
  );
  return { ...utils, apiRef };
}

function renderCheckout() {
  return renderApp({ showCheckout: true });
}

beforeEach(() => {
  localStorage.clear();
  axios.get.mockReset().mockResolvedValue({ data: {} });
  axios.post.mockReset().mockResolvedValue({ data: {} });
  axios.defaults.headers.common = {};
});

describe('Login -> Checkout (chained integration)', () => {
  it('renders the checkout page heading', () => {
    renderCheckout();
    expect(screen.getByText('Xác Nhận Đơn Hàng')).toBeInTheDocument();
  });

  it('uses the token issued by login() to authorize the checkout request', async () => {
    axios.post.mockImplementation((url) => {
      if (url.endsWith('/api/login')) return Promise.resolve({ data: LOGIN_RESPONSE });
      return Promise.resolve({ data: { orderId: 1 } });
    });

    const { apiRef } = renderCheckout();

    // Step A: real login, produces a real token via context state.
    await act(async () => {
      await apiRef.current.auth.login('a@example.com', 'secret');
    });
    expect(axios.post).toHaveBeenCalledWith('http://localhost:3000/api/login', {
      email: 'a@example.com',
      password: 'secret',
    });
    expect(localStorage.getItem('token')).toBe(LOGIN_RESPONSE.token);
    expect(axios.defaults.headers.common['Authorization']).toBe(`Bearer ${LOGIN_RESPONSE.token}`);

    // Step: cart state feeding the same checkout call.
    act(() => {
      apiRef.current.cart.addToCart(PRODUCT, 2);
    });

    fireEvent.click(screen.getByText('Xác Nhận Thanh Toán'));

    await waitFor(() =>
      expect(axios.post).toHaveBeenCalledWith(
        'http://localhost:3000/api/checkout',
        expect.objectContaining({ items: [{ ...PRODUCT, quantity: 2 }] }),
        { headers: { Authorization: `Bearer ${LOGIN_RESPONSE.token}` } },
      ),
    );
  });

  it('sends no Authorization header when checkout happens without a prior login', async () => {
    axios.post.mockResolvedValue({ data: { orderId: 2 } });
    const { apiRef } = renderCheckout();

    act(() => {
      apiRef.current.cart.addToCart(PRODUCT, 1);
    });
    fireEvent.click(screen.getByText('Xác Nhận Thanh Toán'));

    await waitFor(() =>
      expect(axios.post).toHaveBeenCalledWith(
        'http://localhost:3000/api/checkout',
        expect.anything(),
        { headers: {} },
      ),
    );
  });

  it('shows the success screen after a completed checkout', async () => {
    axios.post.mockResolvedValue({ data: { orderId: 3 } });
    renderCheckout();

    fireEvent.click(screen.getByText('Xác Nhận Thanh Toán'));

    await waitFor(() => expect(screen.getByText('Thanh toán thành công!')).toBeInTheDocument());
  });

  it('resets the loading state and re-enables the button after a failed checkout', async () => {
    const alertSpy = vi.spyOn(window, 'alert').mockImplementation(() => {});
    axios.post.mockRejectedValue({ response: { data: { error: 'Hết hàng' } } });
    renderCheckout();

    fireEvent.click(screen.getByText('Xác Nhận Thanh Toán'));

    await waitFor(() => expect(alertSpy).toHaveBeenCalledWith('Lỗi khi thanh toán: Hết hàng'));
    const button = screen.getByText('Xác Nhận Thanh Toán');
    expect(button).not.toBeDisabled();
    alertSpy.mockRestore();
  });

  it('shows no coupon error banner before any coupon has been applied', () => {
    const { container } = renderCheckout();
    expect(container.querySelector('.text-red-600.text-sm')).toBeNull();
  });

  it('clears the Authorization default header once logout() runs after a login()', async () => {
    axios.post.mockImplementation((url) => {
      if (url.endsWith('/api/login')) return Promise.resolve({ data: LOGIN_RESPONSE });
      return Promise.resolve({ data: {} });
    });
    const { apiRef } = renderCheckout();

    await act(async () => {
      await apiRef.current.auth.login('a@example.com', 'secret');
    });
    expect(axios.defaults.headers.common['Authorization']).toBe(`Bearer ${LOGIN_RESPONSE.token}`);

    act(() => {
      apiRef.current.auth.logout();
    });
    await waitFor(() => expect(axios.defaults.headers.common['Authorization']).toBeUndefined());
  });

  it('restores the logged-in user from an existing session token on mount', async () => {
    localStorage.setItem('token', LOGIN_RESPONSE.token);
    axios.get.mockImplementation((url) => {
      if (url.endsWith('/api/users/me')) return Promise.resolve({ data: LOGIN_RESPONSE.user });
      return Promise.resolve({ data: {} });
    });

    const { apiRef } = renderCheckout();

    await waitFor(() => expect(apiRef.current.auth.user).toEqual(LOGIN_RESPONSE.user));
  });

  it('applies a coupon and uses its final_amount (not the raw cart total) at checkout, recording usage', async () => {
    const couponResponse = {
      success: true,
      coupon_id: 42,
      discount_amount: 20000,
      final_amount: 180000,
      message: 'Áp dụng thành công! Giảm 20.000 ₫',
    };
    axios.post.mockImplementation((url) => {
      if (url.endsWith('/api/login')) return Promise.resolve({ data: LOGIN_RESPONSE });
      if (url.endsWith('/api/apply-coupon')) return Promise.resolve({ data: couponResponse });
      return Promise.resolve({ data: { orderId: 4 } });
    });
    axios.get.mockImplementation((url) => {
      if (url.endsWith('/api/users/me')) return Promise.resolve({ data: LOGIN_RESPONSE.user });
      return Promise.resolve({ data: {} });
    });

    // Seed A's output (login + cart) BEFORE Checkout (B) ever mounts, exactly
    // like a real user who logs in and adds items on other pages first.
    const { apiRef } = renderApp({ showCheckout: false });
    await act(async () => {
      await apiRef.current.auth.login('a@example.com', 'secret');
    });
    act(() => {
      apiRef.current.cart.addToCart(PRODUCT, 2);
    });
    act(() => {
      apiRef.current.revealCheckout();
    });

    const couponInput = screen.getByPlaceholderText('Nhập mã giảm giá...');
    fireEvent.change(couponInput, { target: { value: 'sale10' } });
    fireEvent.click(screen.getByText('Áp dụng'));

    await waitFor(() => expect(screen.getByText(/Tiết kiệm/)).toBeInTheDocument());
    // The code is normalized to upper-case and the request carries the real logged-in user id.
    expect(axios.post).toHaveBeenCalledWith('http://localhost:3000/api/apply-coupon', {
      code: 'SALE10',
      total_amount: 200000,
      user_id: LOGIN_RESPONSE.user.id,
    });

    fireEvent.click(screen.getByText('Xác Nhận Thanh Toán'));

    await waitFor(() =>
      expect(axios.post).toHaveBeenCalledWith(
        'http://localhost:3000/api/checkout',
        expect.objectContaining({ total_amount: couponResponse.final_amount, coupon_id: couponResponse.coupon_id }),
        { headers: { Authorization: `Bearer ${LOGIN_RESPONSE.token}` } },
      ),
    );
    await waitFor(() =>
      expect(axios.post).toHaveBeenCalledWith(
        'http://localhost:3000/api/coupon-usage',
        { coupon_id: couponResponse.coupon_id },
        { headers: { Authorization: `Bearer ${LOGIN_RESPONSE.token}` } },
      ),
    );
  });

  it('falls back to the generic coupon error message on a bare network error (no response object)', async () => {
    axios.post.mockImplementation((url) => {
      if (url.endsWith('/api/apply-coupon')) return Promise.reject(new Error('Network Error'));
      return Promise.resolve({ data: {} });
    });
    renderCheckout();

    const couponInput = screen.getByPlaceholderText('Nhập mã giảm giá...');
    fireEvent.change(couponInput, { target: { value: 'sale10' } });
    fireEvent.click(screen.getByText('Áp dụng'));

    await waitFor(() => expect(screen.getByText('Không thể áp dụng mã')).toBeInTheDocument());
  });

  it('falls back to err.message on a bare checkout network error (no response object)', async () => {
    const alertSpy = vi.spyOn(window, 'alert').mockImplementation(() => {});
    axios.post.mockRejectedValue(new Error('Network Error'));
    renderCheckout();

    fireEvent.click(screen.getByText('Xác Nhận Thanh Toán'));

    await waitFor(() => expect(alertSpy).toHaveBeenCalledWith('Lỗi khi thanh toán: Network Error'));
    alertSpy.mockRestore();
  });

  it('shows the coupon error message and does not touch the total when the coupon is rejected', async () => {
    axios.post.mockImplementation((url) => {
      if (url.endsWith('/api/apply-coupon'))
        return Promise.reject({ response: { data: { error: 'Mã giảm giá không tồn tại' } } });
      return Promise.resolve({ data: {} });
    });
    renderCheckout();

    const couponInput = screen.getByPlaceholderText('Nhập mã giảm giá...');
    fireEvent.change(couponInput, { target: { value: 'invalid' } });
    fireEvent.click(screen.getByText('Áp dụng'));

    await waitFor(() => expect(screen.getByText('Mã giảm giá không tồn tại')).toBeInTheDocument());
    expect(screen.queryByText(/Tiết kiệm/)).not.toBeInTheDocument();
  });

  it('shows the exact idle label "Áp dụng" on the coupon button before any click', () => {
    renderCheckout();
    expect(screen.getByRole('button', { name: 'Áp dụng' })).toBeInTheDocument();
  });

  it('does NOT record coupon-usage when a coupon was applied but the user is not logged in (coupon_id present, token missing)', async () => {
    const couponResponse = { success: true, coupon_id: 99, discount_amount: 1000, final_amount: 199000, message: 'ok' };
    axios.post.mockImplementation((url) => {
      if (url.endsWith('/api/apply-coupon')) return Promise.resolve({ data: couponResponse });
      return Promise.resolve({ data: { orderId: 5 } });
    });
    const { apiRef } = renderCheckout();
    act(() => {
      apiRef.current.cart.addToCart(PRODUCT, 2);
    });

    const couponInput = screen.getByPlaceholderText('Nhập mã giảm giá...');
    fireEvent.change(couponInput, { target: { value: 'sale10' } });
    fireEvent.click(screen.getByText('Áp dụng'));
    await waitFor(() => expect(screen.getByText(/Tiết kiệm/)).toBeInTheDocument());

    fireEvent.click(screen.getByText('Xác Nhận Thanh Toán'));
    await waitFor(() =>
      expect(axios.post).toHaveBeenCalledWith(
        'http://localhost:3000/api/checkout',
        expect.objectContaining({ coupon_id: couponResponse.coupon_id }),
        { headers: {} },
      ),
    );
    expect(axios.post).not.toHaveBeenCalledWith(
      'http://localhost:3000/api/coupon-usage',
      expect.anything(),
      expect.anything(),
    );
  });

  it('renders each cart line with its price * quantity subtotal', () => {
    const { apiRef, container } = renderCheckout();
    act(() => {
      apiRef.current.cart.addToCart(PRODUCT, 3);
    });
    expect(container.textContent).toContain(`${PRODUCT.name} x 3`);
    expect(container.textContent).toContain((PRODUCT.price * 3).toLocaleString());
  });

  it('disables the "Áp dụng" button while the coupon code input is empty and enables it once typed', () => {
    renderCheckout();
    expect(screen.getByRole('button', { name: 'Áp dụng' })).toBeDisabled();

    const couponInput = screen.getByPlaceholderText('Nhập mã giảm giá...');
    fireEvent.change(couponInput, { target: { value: 'sale10' } });
    expect(screen.getByRole('button', { name: 'Áp dụng' })).not.toBeDisabled();
  });

  it('shows the transient "..." / "Đang xử lý..." labels while the coupon/checkout requests are in flight', async () => {
    let resolveCoupon;
    axios.post.mockImplementation((url) => {
      if (url.endsWith('/api/apply-coupon')) return new Promise((resolve) => (resolveCoupon = resolve));
      return Promise.resolve({ data: {} });
    });
    renderCheckout();

    const couponInput = screen.getByPlaceholderText('Nhập mã giảm giá...');
    fireEvent.change(couponInput, { target: { value: 'sale10' } });
    fireEvent.click(screen.getByText('Áp dụng'));

    await waitFor(() => expect(screen.getByText('...')).toBeInTheDocument());
    await act(async () => {
      resolveCoupon({ data: { success: true, coupon_id: 1, discount_amount: 0, final_amount: 0, message: 'ok' } });
    });

    let resolveCheckout;
    axios.post.mockImplementation((url) => {
      if (url.endsWith('/api/checkout')) return new Promise((resolve) => (resolveCheckout = resolve));
      return Promise.resolve({ data: {} });
    });
    fireEvent.click(screen.getByText('Xác Nhận Thanh Toán'));
    await waitFor(() => expect(screen.getByText('Đang xử lý...')).toBeInTheDocument());
    await act(async () => {
      resolveCheckout({ data: { orderId: 6 } });
    });
  });
});
