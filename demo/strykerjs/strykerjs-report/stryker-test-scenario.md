# StrykerJS — Kịch bản test & phân tích kết quả (frontend-web)

> Tài liệu này rút gọn từ [`setup-steps.md`](./setup-steps.md), chỉ giữ lại phần **kịch bản
> test / kết quả mong đợi / phân tích / so sánh hiệu quả**. Phần chuẩn bị môi trường xem
> [`stryker-setup-log.md`](./stryker-setup-log.md). Số liệu trong tài liệu này lấy trực tiếp
> từ lần chạy thật, đã đối chiếu khớp với
> `demo/strykerjs/eshop-sut/frontend-web/strykerjs-report.md` và
> `reports/mutation/mutation.json`.

## 1. Hai chức năng được test

| # | Chức năng | File source | Mô tả |
|---|---|---|---|
| 1 | **Giỏ hàng** | `src/context/CartContext.jsx` | Logic nghiệp vụ thuần: thêm sản phẩm vào giỏ (`addToCart`), tính tổng tiền (`cartTotal`), xoá sản phẩm khỏi giỏ (`removeFromCart`), xoá toàn bộ giỏ (`clearCart`). Không phụ thuộc API/localStorage. |
| 2 | **Đăng ký tài khoản / validate mật khẩu** | `src/pages/Register.jsx` | `handleSubmit` kiểm tra mật khẩu mạnh bằng `flawedStrongPasswordRegex` (dòng 15) trước khi gọi `axios.post('http://localhost:3000/api/register', ...)` và điều hướng sang `/login`. Regex này **bị cài lỗi cố ý** trong SUT: yêu cầu khoảng trắng `\s` thay vì ký tự đặc biệt, dù thông báo lỗi ghi "ký tự đặc biệt". |

Chọn 2 chức năng này vì đại diện cho 2 tình huống đối lập của mutation testing:
- **CartContext**: code đơn giản, dễ test đầy đủ → dùng để minh hoạ trường hợp lý tưởng.
- **Register**: có logic validate phức tạp (regex) + một file test viết hời hợt ban đầu → dùng
  để minh hoạ khoảng cách giữa "test pass/có coverage" và "test thật sự phát hiện được lỗi".

## 2. Kết quả mong đợi khi test

| Chức năng | Kỳ vọng trước khi chạy Stryker |
|---|---|
| CartContext | Test hiện có (3 test case: giỏ hàng rỗng ban đầu, thêm sản phẩm + tính tổng, xoá giỏ) sẽ kill gần hết mutant có coverage. `removeFromCart` **cố tình không được test** → mutant tại đó phải rơi vào nhóm `NoCoverage`, không phải `Survived`. |
| Register (test ban đầu — 1 test case, thử đúng 1 password `"abc"`) | Test **pass** và **có coverage** (vì `handleSubmit` được gọi), nhưng vì chỉ assert đúng 1 điều ("có thông báo lỗi hiển thị") nên kỳ vọng phần lớn mutant biến đổi trên regex vẫn **Survived** — minh chứng "coverage cao/test pass không đồng nghĩa test mạnh". |
| Register (test sau khi bổ sung — 9 test case) | Kỳ vọng mutation score tăng đáng kể mà **không sửa một dòng code nào**, vì chỉ thêm/siết assertion. Không kỳ vọng đạt 100% — một số mutant biến đổi ở biên (anchor regex) rất khó kill bằng test case thông thường. |

## 3. Các bước thực hiện test

1. **Baseline**: chạy `npm test` (Vitest) tại `demo/strykerjs/eshop-sut/frontend-web`, xác
   nhận toàn bộ test pass sạch trước khi đụng tới Stryker.
   ```
    RUN  v4.1.10 .../frontend-web
    Test Files  1 passed (1)
         Tests  3 passed (3)
   ```
2. **Cấu hình phạm vi mutate**: `stryker.conf.json` với `mutate` gồm cả 2 file
   (`src/context/CartContext.jsx`, `src/pages/Register.jsx`) — xem
   [`stryker-setup-log.md`](./stryker-setup-log.md#8-tạo-strykerconfjson).
3. **Chạy Stryker**: đứng đúng thư mục `frontend-web`, chạy
   `./node_modules/.bin/stryker run`.
4. **Đọc report**:
   - Bảng tổng hợp trên terminal (clear-text reporter).
   - HTML chi tiết từng mutant: `reports/mutation/mutation.html`.
   - JSON để phân tích số liệu theo mutator: `reports/mutation/mutation.json`.
   - Markdown tự sinh (nếu dùng custom reporter): `strykerjs-report.md`.
5. **Lặp lại có mục tiêu**: với `Register.jsx`, sau khi đọc danh sách mutant `Survived`, viết
   thêm test nhắm đúng từng mutant còn sống, chạy lại Stryker, so sánh số liệu trước/sau (xem
   mục 5 bên dưới).

## 4. Phân tích kết quả

### 4.1. Bảng tổng hợp cuối cùng (sau khi hoàn thiện test cho cả 2 chức năng)

```
------------------|------------------|----------|-----------|------------|----------|----------|
                  | % Mutation score |          |           |            |          |          |
File              |  total | covered | # killed | # timeout | # survived | # no cov | # errors |
------------------|--------|---------|----------|-----------|------------|----------|----------|
All files         |  78.33 |   92.16 |       47 |         0 |          4 |        9 |        0 |
 context          |  85.71 |  100.00 |       12 |         0 |          0 |        2 |        0 |
  CartContext.jsx  |  85.71 |  100.00 |       12 |         0 |          0 |        2 |        0 |
 pages             |  76.09 |   89.74 |       35 |         0 |          4 |        7 |        0 |
  Register.jsx     |  76.09 |   89.74 |       35 |         0 |          4 |        7 |        0 |
------------------|--------|---------|----------|-----------|------------|----------|----------|
```

- **`CartContext.jsx`: 85.71%** (100% trong phần có coverage) — test kill hết mọi mutant mà
  test đi qua; 2 mutant `NoCoverage` là do `removeFromCart` chưa có test, không phải test yếu.
- **`Register.jsx`: 76.09%** (89.74% trong phần có coverage) — sau khi bổ sung test có mục
  tiêu; 4 mutant vẫn sống sót là các trường hợp biên rất khó kill (xem mục 4.3).

### 4.2. Vì sao test ban đầu của Register.jsx yếu (17.39%, 27/46 survived)

Số liệu trích từ lần chạy đầu (chỉ 1 test case `"abc"`), phân theo mutator:

| Loại mutant (mutator) | Vị trí | Số survived | Vì sao survived — thiếu test case gì |
|---|---|---|---|
| `Regex` | dòng 15, `flawedStrongPasswordRegex` | 18 | Test chỉ thử **một** password `"abc"` (rỗng mọi điều kiện). Gần như mọi biến thể mutate của regex vẫn khiến `"abc"` bị từ chối → test vẫn pass dù regex đã sai. Thiếu test theo từng điều kiện riêng lẻ và **thiếu test với password hợp lệ**. |
| `StringLiteral` | dòng 6-9, `useState('')` các field | 4 | Test không bao giờ assert giá trị khởi tạo của input, nên đổi giá trị mặc định không bị phát hiện. |
| `ArrowFunction` | dòng 40, 50, 60 — `onChange` của name/email/password | 3 | Test chỉ tương tác với ô password; `onChange` bị vô hiệu hoá vẫn survive vì kết quả hiển thị lỗi giống hệt trường hợp password sai. |
| `ConditionalExpression` | dòng 17, `if (!regex.test(password))` → `if (true)` | 1 | Test chưa từng thử password hợp lệ, nên ép điều kiện luôn đúng không ảnh hưởng gì. |
| `LogicalOperator` | dòng 33, `{error && <div>...}` → `{error \|\| <div>...}` | 1 | `&&` và `\|\|` cho kết quả giống nhau khi `error` đang truthy; thiếu test khẳng định **không có** div lỗi khi chưa submit. |

### 4.3. Before/after — cải thiện Register.jsx bằng cách viết thêm test (không sửa code)

| Lần chạy | Số test case (Register) | Mutation score `Register.jsx` | Survived |
|---|---|---|---|
| 1 — chỉ 1 test hời hợt | 1 | **17.39%** | 27 |
| 2 — thêm test theo từng điều kiện regex + password hợp lệ + input name/email | 9 | **60.87%** | 11 |
| 3 — thêm assertion "không có khối lỗi lúc đầu" + assert đúng payload `axios.post` | 9 (siết assertion) | **76.09%** | 4 |

Mutation score tăng từ **17.39% → 76.09%** chỉ bằng cách viết thêm/siết test, không sửa một
dòng code nào.

**4 mutant vẫn sống sót sau cùng:**

| Mutator | Mutant | Vì sao vẫn sống |
|---|---|---|
| `Regex` | bỏ anchor `$` cuối regex | Mọi chuỗi test đều "sạch" (không có ký tự thừa sau đoạn hợp lệ) → cần test chuỗi có ký tự thừa **sau**, ví dụ `"Abcdef1 !!!"`. |
| `Regex` | bỏ anchor `^` đầu regex | Tương tự — cần test chuỗi có ký tự thừa **trước**, ví dụ `"!!!Abcdef1 "`. |
| `Regex` | đổi `.*[a-z]` (lookahead đầu) thành `.[a-z]` | Khác biệt cực nhỏ giữa "ký tự bất kỳ ngay trước chữ thường" và "ký tự bất kỳ (0 hoặc nhiều) trước chữ thường" — cần input mà chữ thường nằm xa đầu chuỗi. |
| `StringLiteral` | `navigate('/login')` → `navigate('')` | Test "password hợp lệ" mới assert `axios.post`, chưa assert điều hướng sau khi đăng ký thành công — cần mock `useNavigate` và assert gọi với `'/login'`. |

Đây là ví dụ thực tế cho việc **mutation testing không nhất thiết phải đạt 100%** — 3/4 mutant
còn lại là biến thể regex rất tinh vi ở biên (anchor/quantifier), phù hợp để nói về chi phí/lợi
ích khi đẩy mutation score lên rất cao.

## 5. So sánh hiệu quả test giữa 2 chức năng

| Tiêu chí | CartContext.jsx (Giỏ hàng) | Register.jsx (Đăng ký) |
|---|---|---|
| Mutation score (total) | 85.71% | 76.09% |
| Mutation score (covered) | **100%** | 89.74% |
| Survived | 0 | 4 |
| NoCoverage | 2 (`removeFromCart` chưa test) | 7 (nhánh lỗi API `catch`, chưa test) |
| Loại lỗ hổng minh hoạ | Thiếu **coverage** — dễ phát hiện bằng công cụ đo coverage thông thường (Istanbul/Jest Coverage) | Có **coverage đầy đủ + test pass** nhưng ban đầu **assertion hời hợt** — công cụ đo coverage thuần tuý **không thể phát hiện** loại lỗ hổng này |
| Cách khắc phục | Thêm test cho `removeFromCart` | Viết test theo từng điều kiện (boundary, equivalence class), không chỉ 1 kịch bản |

**Kết luận (Test Effectiveness):**

- `CartContext.jsx` minh hoạ trường hợp **"NoCoverage"**: phần code có test thì mutation score
  đạt tuyệt đối (100%); phần chưa test lộ rõ ngay dưới dạng `NoCoverage`, dễ phát hiện.
- `Register.jsx` minh hoạ trường hợp **"Survived"** — loại lỗ hổng nguy hiểm hơn: có test, test
  pass, có coverage, nhưng vì assertion quá hời hợt (ban đầu 1 test, 1 assertion) nên chỉ kill
  được 22.86% mutant có coverage. Đây là loại lỗ hổng mà công cụ đo *code coverage* thuần tuý
  không thể phát hiện, vì coverage chỉ quan tâm dòng code có được chạy qua hay không, không
  quan tâm assertion có đủ mạnh để bắt lỗi hay không.
- Cùng một file, chỉ bằng cách viết thêm/siết test (không sửa code), mutation score có thể tăng
  từ 17.39% lên 76.09% — đây là bằng chứng thực nghiệm rõ ràng nhất cho luận điểm: **code
  coverage cao (hoặc test pass) không đồng nghĩa test suite có khả năng phát hiện lỗi logic.**

