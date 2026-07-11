import { describe, it, expect } from 'vitest';
import { renderHook, act } from '@testing-library/react';
import { CartProvider, useCart } from '../../src/context/CartContext';

const wrapper = ({ children }) => <CartProvider>{children}</CartProvider>;

describe('CartContext', () => {
  it('starts with an empty cart', () => {
    const { result } = renderHook(() => useCart(), { wrapper });
    expect(result.current.cart).toEqual([]);
    expect(result.current.cartTotal).toBe(0);
  });

  it('adds a product to the cart and updates the total', () => {
    const { result } = renderHook(() => useCart(), { wrapper });

    act(() => {
      result.current.addToCart({ id: 1, name: 'Shirt', price: 100000 }, 2);
    });

    expect(result.current.cart).toHaveLength(1);
    expect(result.current.cartTotal).toBe(200000);
  });

  it('clears the cart', () => {
    const { result } = renderHook(() => useCart(), { wrapper });

    act(() => {
      result.current.addToCart({ id: 1, name: 'Shirt', price: 100000 }, 1);
      result.current.clearCart();
    });

    expect(result.current.cart).toEqual([]);
    expect(result.current.cartTotal).toBe(0);
  });
});
