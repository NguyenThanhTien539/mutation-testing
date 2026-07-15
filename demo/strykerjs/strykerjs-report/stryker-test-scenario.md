# Kịch bản Mutation Testing: Login → Checkout (eshop-sut)

Ứng dụng: `eshop-sut/frontend-web` (React + Vite, test runner Vitest, mutation testing StrykerJS 9.6).
Cặp hàm tuần tự được chọn: **A = `login()`** (`src/context/AuthContext.jsx`) → **B = `handleCheckout()`** (`src/pages/Checkout.jsx`). `handleCheckout` phụ thuộc trực tiếp vào state (`token`, `user`) mà `login()` tạo ra — đúng dạng "cùng một phiên đăng nhập" mà bài toán yêu cầu.

---

## Bước 0 — Chọn cặp hàm tuần tự

| | Hàm | File | Vai trò |
|---|---|---|---|
| A | `login(email, password)` | `src/context/AuthContext.jsx:26-35` | Gọi `POST /api/login`, lưu `token`/`user` vào state + `localStorage`, gắn `Authorization` header mặc định cho axios |
| B | `handleCheckout()` | `src/pages/Checkout.jsx:40-66` | Đọc `token`/`user` từ `useAuth()` (state do A tạo) để gắn header `Authorization: Bearer <token>` khi gọi `POST /api/checkout`, và rẽ nhánh gọi thêm `POST /api/coupon-usage` nếu có coupon |

B **không thể được kiểm thử đúng đắn nếu không có A chạy trước** — nếu test chỉ gọi B một mình (không login), `token` luôn `null`, và nhánh `headers: token ? {...} : {}` chỉ bao giờ chạm nhánh `else`.

Cấu hình `stryker.conf.json` để chỉ mutate 2 file này:

```json
{
  "testRunner": "vitest",
  "coverageAnalysis": "perTest",
  "mutate": ["src/context/AuthContext.jsx", "src/pages/Checkout.jsx"]
}
```

---

## Bước 1 — Baseline mutation run (test suite "yếu")

Trước khi có test chained, ta viết một test **hời hợt** để mô phỏng đúng thực trạng "coverage tồn tại nhưng không kiểm chứng gì":

```jsx
// test/pages/Checkout.test.jsx (baseline — sau này sẽ bị thay thế)
describe('Checkout - baseline smoke test', () => {
  it('renders the checkout page heading', () => {
    renderCheckout();
    expect(screen.getByText('Xác Nhận Đơn Hàng')).toBeInTheDocument();
  });
  it('renders the checkout confirmation button', () => {
    renderCheckout();
    expect(screen.getByText('Xác Nhận Thanh Toán')).toBeInTheDocument();
  });
});
```

Chạy `stryker run` → 109 mutant sinh ra trên 2 file:

| File | Total | Killed | Survived | Timeout | No coverage | Score (killed/total) | Score (Stryker chính thức, killed+timeout/total) |
|---|---|---|---|---|---|---|---|
| AuthContext.jsx | 22 | 1 | 3 | 6 | 12 | 4.55% | 31.82% |
| Checkout.jsx | 87 | 3 | 7 | 12 | 65 | 3.45% | 17.24% |
| **Tổng** | **109** | **4** | **10** | **18** | **77** | **3.67%** | **20.18%** |

→ **77/109 mutant (71%) hoàn toàn "no coverage"** dù ứng dụng có thể build, chạy, và trang Checkout "hiển thị đúng" khi review bằng mắt.

---

## Bước 2 — Liệt kê mutant sống sót (Survived, không phải NoCoverage)

Đây là các mutant mà test **có chạy qua** dòng code đó nhưng không phát hiện được thay đổi hành vi:

### `AuthContext.jsx`
| Dòng | Loại | Thay đổi |
|---|---|---|
| 21 | BlockStatement | thân `if (token)` bị thay bằng `{}` |
| 24 | ArrayDeclaration | dependency array `[token]` → `[]` |
| 44 | ObjectLiteral | `value={{ user, token, login, logout }}` → `value={{}}` |

### `Checkout.jsx`
| Dòng | Loại | Thay đổi |
|---|---|---|
| 68 | ConditionalExpression | `if (success)` → `if (false)` |
| 121 | StringLiteral | `'Áp dụng'` → `""` |
| 124 | ConditionalExpression / LogicalOperator | `couponError && (...)` → `{true}` / `{false}` / `couponError \|\| (...)` |
| 127 | ConditionalExpression | `couponResult && (...)` → `{true}` / `{false}` |

## Bước 3 — Phân tích nguyên nhân

Test smoke-test baseline chỉ `render()` và kiểm tra 2 đoạn text tĩnh. Nó **không hề**:
- Gọi `login()` → nên `AuthContext.Provider`'s `value` object không bao giờ bị đọc field nào (`login`/`logout`/`user`/`token` đều không dùng) → mutant `{{}}` sống.
- Kích hoạt submit checkout → nhánh `if (success)` không bao giờ chạm tới trạng thái `true`.
- Nhập/áp mã coupon → `couponError`, `couponResult` luôn ở giá trị khởi tạo, không phân biệt được nhánh render có/không có.

---

## Bước 4 — Viết test integration (Login → Checkout thật)

File: `test/pages/Checkout.test.jsx` (bản đầy đủ, 17 test case). Điểm mấu chốt — một `Harness` component nằm **trong cùng cây Provider** với `Checkout`, expose thẳng `useAuth()`/`useCart()` cho test:

```jsx
function Harness({ apiRef, initiallyVisible }) {
  const [visible, setVisible] = useState(initiallyVisible);
  apiRef.current = { auth: useAuth(), cart: useCart(), revealCheckout: () => setVisible(true) };
  return visible ? <Checkout /> : null;
}
```

Test tiêu biểu — **gọi A thật, dùng output của A để lái B**:

```jsx
it('uses the token issued by login() to authorize the checkout request', async () => {
  axios.post.mockImplementation((url) => {
    if (url.endsWith('/api/login')) return Promise.resolve({ data: LOGIN_RESPONSE });
    return Promise.resolve({ data: { orderId: 1 } });
  });
  const { apiRef } = renderCheckout();

  // Bước A: login thật, tạo token thật qua context state.
  await act(async () => { await apiRef.current.auth.login('a@example.com', 'secret'); });

  // Bước B: checkout dùng chính token đó, không phải giá trị hard-code.
  act(() => { apiRef.current.cart.addToCart(PRODUCT, 2); });
  fireEvent.click(screen.getByText('Xác Nhận Thanh Toán'));

  await waitFor(() =>
    expect(axios.post).toHaveBeenCalledWith(
      'http://localhost:3000/api/checkout',
      expect.objectContaining({ items: [{ ...PRODUCT, quantity: 2 }] }),
      { headers: { Authorization: `Bearer ${LOGIN_RESPONSE.token}` } },
    ),
  );
});
```

Một lưu ý kỹ thuật quan trọng phát hiện được *nhờ chính việc viết test này*: `Checkout.jsx` dùng `useState(cartTotal)` để khởi tạo `editableTotal` — giá trị này **chỉ được chụp một lần lúc mount**, không phản ứng lại khi giỏ hàng thay đổi sau đó. Vì vậy test coupon phải **seed A (login + addToCart) trước khi mount Checkout** (dùng `revealCheckout()`), giống hệt hành vi thật: người dùng đăng nhập và thêm hàng vào giỏ ở các trang khác trước khi vào `/checkout`.

Các test khác trong bộ (tóm tắt):
- Checkout không có Authorization header khi chưa login.
- Trang "Thanh toán thành công!" hiển thị sau khi checkout OK.
- `setLoading(false)` chạy lại sau lỗi checkout (nút không bị kẹt "Đang xử lý...").
- Không có banner lỗi coupon khi chưa áp mã nào.
- `logout()` xoá `Authorization` header mặc định của axios sau khi đã login.
- Session được khôi phục từ `localStorage` lúc mount (`GET /api/users/me`).
- Áp coupon hợp lệ → checkout dùng `final_amount` của coupon (không phải tổng giỏ hàng thô) + gọi `coupon-usage`.
- Áp coupon nhưng **chưa login** (có `coupon_id`, không có `token`) → **không** gọi `coupon-usage` (phân biệt `&&` thật với `||` giả).
- Lỗi mạng không có `response` object → rơi về thông báo lỗi mặc định (không throw).
- Nhãn nút chuyển tạm thời "..."/"Đang xử lý..." trong lúc request đang chạy.

---

## Bước 5 — Chạy lại Stryker, xác nhận diệt mutant

```
------------------|------------------|----------|-----------|------------|----------|
File              |  total | covered | # killed | # timeout | # survived | # no cov |
------------------|--------|---------|----------|-----------|------------|----------|
All files         |  90.83 |   94.29 |       61 |        38 |          6 |        4 |
 AuthContext.jsx   |  95.45 |  100.00 |       15 |         6 |          0 |        1 |
 Checkout.jsx      |  89.66 |   92.86 |       46 |        32 |          6 |        3 |
```

Mutation score (Stryker, killed+timeout/total): **20.18% → 90.83%** (+70.65 điểm phần trăm).
`AuthContext.jsx`: **31.82% → 95.45%**. `Checkout.jsx`: **17.24% → 89.66%**.

Tất cả 10 mutant "Survived" ban đầu đã bị diệt.

## Bước 6 — Lặp lại cho mutant còn sống sót

Vòng lặp mở rộng test đã diệt gần hết nhưng phát sinh thêm mutant "Survived" mới ở những dòng **lần đầu được coverage** (đúng minh chứng cho coverage illusion — xem `coverage-vs-mutation-stryker.md`). Sau nhiều vòng bổ sung assertion (exact body request, phân biệt `&&`/`||`, network-error không có `response`, nhãn nút tạm thời...), còn lại **6 mutant sống sót**, tất cả đều là các biến thể gần tương đương không đáng đánh đổi thêm độ phức tạp test:

| File | Dòng | Loại | Ghi chú |
|---|---|---|---|
| Checkout.jsx | 29 | `couponCode.trim().toUpperCase()` → `couponCode.toUpperCase()` | Input test không có khoảng trắng thừa nên `.trim()` là no-op quan sát được |
| Checkout.jsx | 35 | `err.response?.data?.error` → `err.response?.data.error` | Chỉ khác khi `response` tồn tại nhưng `response.data` là `null`/`undefined` — chưa có test dựng đúng shape lỗi đó |
| Checkout.jsx | 63 | tương tự dòng 35, cho nhánh lỗi checkout | như trên |
| Checkout.jsx | 73 | `onClick={() => navigate('/')}` → `() => undefined` | Nút "Quay lại trang chủ" trên màn hình thành công chưa được click trong test |
| Checkout.jsx | 113 | `onChange` handler, `setCouponError('')` → chuỗi khác | Giá trị reset che khuất bởi các thay đổi state khác cùng lúc trong test hiện có |
| Checkout.jsx | 118 | `!couponCode.trim()` → `!couponCode` | Input test luôn "sạch" (không khoảng trắng) nên hai biểu thức tương đương quan sát được |

→ Đây là ví dụ thực tế cho thấy mutation testing hiếm khi đạt 100%, và phần còn lại cần được đánh giá và phân loại thay vì cố diệt bằng mọi giá.

---

## Bước 7 — Code Coverage trên cùng 2 hàm, cùng test suite ban đầu

Cài `@vitest/coverage-istanbul` và khai báo `test.coverage.provider: 'istanbul'` trong `vite.config.js`, chạy coverage **với đúng bộ test baseline (yếu) của Bước 1**, giới hạn vào 2 file mutate:

```
npx vitest run --coverage --coverage.include='src/context/AuthContext.jsx' --coverage.include='src/pages/Checkout.jsx'
```

Khi đó ta có kết quả sau:

```
File              | % Stmts | % Branch | % Funcs | % Lines
------------------|---------|----------|---------|--------
AuthContext.jsx   |   50.00 |    50.00 |   42.85 |   47.82
Checkout.jsx      |   33.33 |    25.00 |   14.28 |   35.89
All files         |   39.39 |    26.47 |   28.57 |   40.32
```

## Bước 8 — So sánh Coverage vs Mutation Score

Xem chi tiết đầy đủ trong `coverage-vs-mutation-stryker.md`. Tóm tắt:

| Mốc | Line Coverage | Mutation Score (tính luôn timeout) | Mutation Score (chỉ tính killed) |
|---|---|---|---|
| Trước integrate | **40.32%** | 20.18% | 3.67% |
| Sau integrate | **91.93%** | 90.83% | 55.96% |

Bằng chứng "coverage illusion" rõ nhất: ở mốc "Trước", coverage đã là 40% — component vẫn render, nhánh `if/else` cơ bản vẫn được duyệt qua  — nhưng **mutation score chỉ 3.67-20.18%**, vì test không kiểm tra bất kỳ giá trị cụ thể nào. Coverage đo "code có chạy", mutation testing đo "test có phát hiện được lỗi".

---

## Bước 9 — Tệp bằng chứng

- Test file: `test/pages/Checkout.test.jsx` (17 test case, bản đầy đủ)
- Config: `stryker.conf.json` (mutate = AuthContext.jsx + Checkout.jsx)
- Báo cáo mutation: `strykerjs-report-before.md`, `strykerjs-report-after.md`, `reports/mutation-before/`, `reports/mutation-after/` 
- Báo cáo coverage: `coverage-before/`, `coverage-after/`
- Tài liệu tổng hợp: `stryker-test-scenario.md` , `coverage-vs-mutation-stryker.md`, `stryker-demo-script.md`
