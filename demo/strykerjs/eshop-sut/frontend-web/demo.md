# Demo trực tiếp: Mutation Testing Login → Checkout

File này để **mở song song với terminal khi demo** — mỗi bước có: lệnh gõ y nguyên + lời thoại gợi ý để nói trôi chảy. Tổng thời lượng ~12-15 phút.

> Thư mục làm việc cho mọi lệnh: `eshop-sut/frontend-web`
> ```bash
> cd eshop-sut/frontend-web
> ```

> ⚠️ **Luôn dọn sandbox của Stryker trước khi chạy `vitest run` bất kỳ lúc nào trong buổi demo:**
> ```bash
> rm -rf .stryker-tmp
> ```
> Nếu bỏ qua bước này, Vitest sẽ quét luôn các bản sao test nằm trong `.stryker-tmp/sandbox-*/` từ lần chạy Stryker trước, khiến số lượng test/file hiện ra **gấp nhiều lần con số thật** (ví dụ 12 file / 101 test thay vì 3 file / 29 test) — dễ gây hoang mang ngay trên sân khấu. Mỗi lệnh `stryker run` trong file này đều tự kèm `rm -rf .stryker-tmp` phía trước, nhưng nếu bạn chạy `npx vitest run` một mình (ví dụ để demo lại), hãy nhớ xoá `.stryker-tmp` trước.

---

## 0. Mở đầu (nói trước khi gõ lệnh nào)

> "Hôm nay em demo mutation testing trên một cặp hàm có phụ thuộc tuần tự thật trong ứng dụng eshop: **`login()`** tạo ra token, và **`handleCheckout()`** dùng chính token đó để xác thực đơn hàng. Đây không phải hai hàm độc lập — nếu test `handleCheckout` mà không thật sự đăng nhập trước, phần lớn logic quan trọng sẽ không bao giờ được kiểm chứng đúng cách. Em sẽ cho thấy: coverage cao không có nghĩa là test tốt — và mutation testing chứng minh điều đó bằng số liệu cụ thể."

Mở nhanh 2 file nguồn cho khán giả thấy:
```bash
code src/context/AuthContext.jsx src/pages/Checkout.jsx
```
> "Dòng 26-35 của AuthContext là `login()` — gọi API, lưu token vào state và localStorage. Dòng 40-66 của Checkout là `handleCheckout()` — đọc `token` từ context đó để gắn header `Authorization: Bearer <token>` khi gọi API checkout."

---

## 1. Cấu hình Stryker — chỉ mutate 2 file này

```bash
cat stryker.conf.json
```
> "Em giới hạn phạm vi mutate chỉ vào 2 file này để báo cáo tập trung, không bị loãng bởi các file khác trong dự án."

---

## 2. Trạng thái BASELINE — test chỉ render, không assert hành vi

Đổi tạm sang bộ test "yếu" để mô phỏng lại điểm xuất phát (bộ test đầy đủ hiện tại sẽ được backup và khôi phục ở Bước 5):

```bash
cp test/pages/Checkout.test.jsx test/pages/Checkout.test.jsx.demo-full.bak
cp test/pages/Checkout.baseline.test.jsx.txt test/pages/Checkout.test.jsx
```

Cho khán giả xem nội dung file baseline:
```bash
cat test/pages/Checkout.test.jsx
```
> "Đây là kiểu test rất phổ biến trong thực tế: chỉ `render()` component rồi kiểm tra vài dòng chữ tĩnh có xuất hiện hay không. Nó chạy được, pass, và nhìn coverage report sẽ thấy xanh khá nhiều — nhưng nó không hề assert bất kỳ hành vi nghiệp vụ nào."

### 2.1 Chạy test suite bình thường — xem tỷ lệ pass

```bash
rm -rf .stryker-tmp
npx vitest run
```
> "Trước tiên, chạy test theo cách thông thường. Kết quả: **pass 100%**. Nếu chỉ nhìn con số này, ai cũng sẽ nghĩ code chạy đúng, yên tâm merge. Đây chính là cái bẫy — **một bộ test yếu vẫn xanh 100% như thường**, vì nó không hề kiểm tra điều gì đủ cụ thể để có thể fail. Pass rate không nói lên được test có *chất lượng* hay không, chỉ nói lên test đó có tự mâu thuẫn với chính nó hay không."

### 2.2 Chạy coverage với bộ test yếu

```bash
npx vitest run --coverage --coverage.include='src/context/AuthContext.jsx' --coverage.include='src/pages/Checkout.jsx'
```
> "Chú ý số liệu: Line coverage khoảng **40%**. Nhớ con số này."

### 2.3 Chạy Stryker với bộ test yếu

```bash
rm -rf .stryker-tmp
node_modules/.bin/stryker run
```
*(Windows PowerShell nếu không có Git Bash: `node_modules\.bin\stryker.cmd run`)*

Trong lúc chờ (~1 phút), nói:
> "StrykerJS sẽ tạo ra các phiên bản 'đột biến' của code — đổi `if` thành `true/false`, đổi chuỗi, đổi toán tử — rồi chạy lại toàn bộ test suite trên từng phiên bản. Nếu test vẫn pass dù code đã bị đổi sai, nghĩa là test đó không phát hiện được lỗi — mutant đó 'sống sót'."

Khi kết quả hiện ra:
> "Coverage vừa rồi là 40%, nhưng mutation score chỉ khoảng **20%** — và nếu tính khắt khe, chỉ tính mutant bị *diệt trực tiếp* bởi assertion, con số chỉ còn **3.67%**. Đây chính là khoảng cách giữa 'code có chạy' và 'test có kiểm chứng đúng'."

Mở report HTML để chỉ trực quan 1 mutant sống sót tiêu biểu:
```bash
start reports/mutation/mutation.html
```
> "Em bấm vào `Checkout.jsx`, dòng 68: `if (success)`. Stryker đổi thành `if (false)` — nghĩa là màn hình 'Thanh toán thành công' không bao giờ hiển thị được nữa — vậy mà test vẫn pass, vì chưa từng có test nào bấm nút thanh toán."

---

## 3. Viết test tích hợp (chained) — điểm nhấn chính của demo

Khôi phục bộ test đầy đủ:
```bash
cp test/pages/Checkout.test.jsx.demo-full.bak test/pages/Checkout.test.jsx
rm test/pages/Checkout.test.jsx.demo-full.bak
```

Mở file để show đoạn code cốt lõi:
```bash
code test/pages/Checkout.test.jsx
```

Chỉ vào hàm `Harness` (đầu file):
> "Ý tưởng cốt lõi: em tạo một component `Harness` nằm **bên trong cùng cây Provider** với `Checkout`, để test có thể lấy tay `useAuth()` và `useCart()` thật — không mock context, chỉ mock tầng network (`axios`)."

Chỉ vào test `'uses the token issued by login() to authorize the checkout request'`:
> "Test này làm đúng 2 bước tuần tự: **Bước A** — gọi `login()` thật, để context tự sinh ra token thật từ response API giả lập. **Bước B** — bấm nút thanh toán, rồi assert rằng request `/api/checkout` được gửi kèm đúng header `Authorization: Bearer <token đó>` — không phải giá trị hard-code, mà là giá trị thực sự đến từ bước A."

Có thể lướt nhanh qua 2-3 test khác đáng chú ý:
- `'applies a coupon and uses its final_amount ... recording usage'` — chuỗi 3 hàm nối tiếp: login → apply coupon → checkout.
- `'does NOT record coupon-usage when ... token missing'` — test phân biệt `&&` thật với `||` giả (một loại mutant khó diệt).

---

## 4. Re-run — chứng minh điểm số tăng vọt

### 4.1 Chạy test suite bình thường — pass rate vẫn 100%

```bash
rm -rf .stryker-tmp
npx vitest run
```
> "Chạy lại test suite bình thường — vẫn **pass 100%**, y hệt như lúc nãy với bộ test yếu. Đây là điều em muốn nhấn mạnh: nhìn vào con số pass rate, hai bộ test này **không phân biệt được** — cả hai đều xanh. Sự khác biệt thật sự chỉ lộ ra khi chạy coverage và mutation testing."

### 4.2 Coverage sau khi có test thật

```bash
npx vitest run --coverage --coverage.include='src/context/AuthContext.jsx' --coverage.include='src/pages/Checkout.jsx'
```
> "Line coverage giờ là khoảng **92%**."

### 4.3 Mutation score sau khi có test thật

```bash
rm -rf .stryker-tmp
node_modules/.bin/stryker run
```
> "Trong lúc chờ khoảng 2-3 phút — lần này Stryker chạy 17 test case trên 109 mutant, nhiều hơn hẳn lần trước."

Khi có kết quả:
> "Mutation score nhảy từ **20% lên 90.83%**. AuthContext.jsx từ 31.82% lên **95.45%**, Checkout.jsx từ 17.24% lên **89.66%**. Toàn bộ 10 mutant sống sót ban đầu đã bị diệt."

---

## 5. Chốt lại: "Coverage illusion"

Mở bảng so sánh đã chuẩn bị sẵn:
```bash
code coverage-vs-mutation-stryker.md
```

> "Đây là bảng tổng kết. Điều quan trọng nhất không phải là hai con số đều tăng — mà là **khoảng cách giữa chúng thu hẹp lại**. Ban đầu coverage 40% nhưng mutation score chỉ 20% — chênh 20 điểm. Sau khi có test thật, coverage 92% và mutation score 91% — chênh chưa đầy 1 điểm. Khi test chỉ *chạy qua* code, hai chỉ số tách xa nhau. Khi test *thật sự kiểm chứng hành vi*, hai chỉ số hội tụ."

Câu chốt (nói chậm, nhấn mạnh):
> **"Cả hai bộ test — yếu và mạnh — đều pass 100% khi chạy `vitest run`. Pass rate không phân biệt được chúng. Code coverage cho biết code có được thực thi. Mutation testing cho biết test có phát hiện được lỗi hay không. Một dòng code có thể tô xanh 100%, một bộ test có thể xanh 100%, mà không có một dòng `expect()` nào thực sự kiểm tra giá trị nó tạo ra."**

Nếu còn thời gian, nói thêm về 6 mutant còn sống sót cuối cùng:
> "Vẫn còn 6 mutant sống sót sau tất cả các vòng lặp bổ sung test — nhưng đây là các biến thể gần-tương đương, ví dụ `.trim()` khi input test không có khoảng trắng thừa nên không quan sát được khác biệt. Mutation testing trong thực tế hiếm khi đạt 100% — quan trọng là biết *tại sao* mutant còn sống, không phải cố diệt bằng mọi giá."

---

## Dọn dẹp sau demo

```bash
rm -rf .stryker-tmp
git status
```
*(Kiểm tra không còn file `.bak` sót lại trong `test/pages/` trước khi commit.)*

---

## Bảng số liệu tóm tắt (in ra giấy / để trên màn hình phụ)

| | Vitest pass rate | Line Coverage | Mutation Score (Stryker) |
|---|---:|---:|---:|
| Trước (test hời hợt, 2 test) | 100% (2/2) | 40.32% | 20.18% |
| Sau (test chained, 17 test) | 100% (17/17) | 91.93% | 90.83% |

> Lưu ý khi trình bày bảng này: cột "Vitest pass rate" **cố tình giống hệt nhau** ở cả hai dòng — đó chính là luận điểm của demo, không phải sai sót.

## Danh sách lệnh (copy nhanh, không cần đọc lại từng bước)

```bash
cd eshop-sut/frontend-web
rm -rf .stryker-tmp

# --- Baseline ---
cp test/pages/Checkout.test.jsx test/pages/Checkout.test.jsx.demo-full.bak
cp test/pages/Checkout.baseline.test.jsx.txt test/pages/Checkout.test.jsx
npx vitest run
npx vitest run --coverage --coverage.include='src/context/AuthContext.jsx' --coverage.include='src/pages/Checkout.jsx'
rm -rf .stryker-tmp && node_modules/.bin/stryker run
start reports/mutation/mutation.html

# --- Khôi phục test đầy đủ ---
cp test/pages/Checkout.test.jsx.demo-full.bak test/pages/Checkout.test.jsx
rm test/pages/Checkout.test.jsx.demo-full.bak

# --- Sau ---
rm -rf .stryker-tmp
npx vitest run
npx vitest run --coverage --coverage.include='src/context/AuthContext.jsx' --coverage.include='src/pages/Checkout.jsx'
rm -rf .stryker-tmp && node_modules/.bin/stryker run
start reports/mutation/mutation.html
start coverage/index.html
```
