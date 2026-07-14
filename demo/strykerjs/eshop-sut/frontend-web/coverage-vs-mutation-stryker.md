# Coverage vs Mutation Score — bằng chứng "coverage illusion"

Phạm vi: `src/context/AuthContext.jsx` + `src/pages/Checkout.jsx` (cặp hàm Login → Checkout).
Công cụ: coverage qua `@vitest/coverage-istanbul` (`vitest run --coverage`, `provider: 'istanbul'` — cùng công cụ Istanbul/nyc mà `jest --coverage` dùng) và StrykerJS 9.6 (`vitest` test runner, `coverageAnalysis: perTest`).

## 1. Bảng số liệu

| Chỉ số | Trước (test hời hợt, chỉ render) | Sau (test chained Login→Checkout) | Δ |
|---|---:|---:|---:|
| Statement coverage | 39.39% | 90.90% | +51.51 |
| **Line coverage** | **40.32%** | **91.93%** | **+51.61** |
| Branch coverage | 26.47% | 97.05% | +70.58 |
| Function coverage | 28.57% | 78.57% | +50.00 |
| Mutation score (Stryker, killed+timeout/total) | 20.18% | 90.83% | +70.65 |
| Mutation score (killed-only/total, khắt khe) | 3.67% | 55.96% | +52.29 |
| Mutant "Survived" (chạy qua nhưng không bị diệt) | 10 | 6 | −4 |
| Mutant "No coverage" | 77 | 4 | −73 |

Nguồn số liệu: `coverage-before/`, `coverage-after/` (HTML report Vitest), `strykerjs-report-before.md`, `strykerjs-report-after.md`.

## 2. Điểm mấu chốt: "Trước" — coverage 40% nhưng mutation score chỉ 3.67-20.18%

Test baseline chỉ có 2 câu:
```jsx
it('renders the checkout page heading', () => { ... expect(screen.getByText('Xác Nhận Đơn Hàng')).toBeInTheDocument(); });
it('renders the checkout confirmation button', () => { ... expect(screen.getByText('Xác Nhận Thanh Toán')).toBeInTheDocument(); });
```

Chỉ 2 `render()` này đã kéo statement coverage lên **38.46%** — vì `render()` chạy toàn bộ thân component (khai báo state, tính `cartTotal`, JSX cho các nhánh mặc định) dù không có bất kỳ `expect` nào kiểm tra logic. Cụ thể các dòng "xanh" (covered) trong báo cáo Istanbul/V8 nhưng vẫn có mutant "Survived" tương ứng ở lần chạy Stryker đầu tiên:

| Dòng | Trạng thái Coverage | Trạng thái Mutation | Ý nghĩa |
|---|---|---|---|
| `Checkout.jsx:68` `if (success)` | Covered (nhánh `false` được chạy khi mount) | **Survived** — mutant `if (false)` | Coverage chỉ ghi nhận "dòng if chạy", không biết nhánh `true` (trang thành công) có bao giờ được kiểm chứng hay không |
| `Checkout.jsx:124` `{couponError && (...)}` | Covered | **Survived** — cả `{true}`, `{false}` và mutant `\|\|` | JSX conditional render luôn "chạy qua" mỗi lần render dù `couponError` không đổi giá trị bao giờ |
| `AuthContext.jsx:44` `value={{ user, token, login, logout }}` | Covered (object luôn được tạo mỗi render) | **Survived** — mutant `value={{}}` | Object literal "chạy" nhưng không ai *đọc* field nào của nó → coverage xanh, hành vi sai vẫn lọt |

Đây chính là "coverage illusion" theo lý thuyết: **coverage đo được code có được *thực thi***, còn **mutation testing đo được test có *khẳng định đúng hành vi* của code đó hay không**. Một dòng có thể tô xanh 100% mà không có một `expect()` nào chạm tới giá trị nó tạo ra.

## 3. "Sau" — cả hai chỉ số cùng tăng, và hội tụ gần nhau

Sau khi thay bằng bộ test chained (17 test case, gọi thật `login()` rồi dùng `token`/`user` để lái `handleCheckout()`):

- Line coverage: 40.32% → **91.93%**
- Mutation score (Stryker): 20.18% → **90.83%**

Khoảng cách giữa 2 chỉ số thu hẹp từ **20.14 điểm phần trăm** (40.32 − 20.18) xuống còn **1.10 điểm phần trăm** (91.93 − 90.83). Khi test thật sự assert vào giá trị trả về / side-effect (body request, header, DOM sau tương tác) thay vì chỉ render, hai chỉ số hội tụ — vì lúc đó "code chạy" và "hành vi được kiểm chứng" gần như trùng nhau.

Phần chênh lệch còn lại (91.93% coverage vs 90.83% mutation score) đến từ 6 mutant "Survived" còn sót (xem `stryker-test-scenario.md` Bước 6) — toàn bộ đều nằm trên các dòng **đã covered nhưng biến thể mutant tạo ra hành vi quan sát-tương đương** trong đúng kịch bản test hiện có (vd. `.trim()` trên input không có khoảng trắng thừa). Đây là minh chứng thứ hai của cùng một nguyên lý, ở quy mô nhỏ hơn: coverage cao không đảm bảo triệt tiêu hoàn toàn khoảng trống kiểm thử.

## 4. Kết luận

1. Code coverage là điều kiện **cần** nhưng không **đủ**: 100% coverage vẫn có thể để lọt logic sai nếu test không assert giá trị.
2. Mutation score buộc test phải "trả lời đúng câu hỏi": nếu hành vi bị thay đổi (mutant), test có báo đỏ không?
3. Cách hiệu quả nhất để tăng mutation score không phải là viết thêm test render thêm dòng code, mà là **viết assertion cụ thể vào giá trị/side-effect thực tế** — đúng như cách bộ test chained Login → Checkout đã làm (kiểm tra header `Authorization`, body request, `localStorage`, DOM sau tương tác thật).
