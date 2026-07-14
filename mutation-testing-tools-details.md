# Mutation Testing: Nguyên Lý Hoạt Động và Hai Công Cụ Tiêu Biểu (StrykerJS & mutmut)

## 1. Nguyên lý hoạt động chung

Bất kể ngôn ngữ hay công cụ nào, mutation testing đều theo một quy trình cốt lõi:

### Bước 1 — Sinh "mutant" (đột biến)
Công cụ phân tích cú pháp (AST) của code nguồn, sau đó áp dụng các mutation operator — những phép biến đổi nhỏ mô phỏng lỗi lập trình viên hay mắc phải:

| Loại operator | Ví dụ |
|---|---|
| Đổi toán tử so sánh | `>` ↔ `>=`, `==` ↔ `!=` |
| Đổi toán tử số học | `+` ↔ `-`, `*` ↔ `/` |
| Đổi toán tử logic | `&&` ↔ `\|\|` |
| Đổi hằng số | `0` → `1`, `true` → `false` |
| Xóa câu lệnh | `x++;` → (xóa) |
| Đổi giá trị trả về | `return price` → `return 0` |

Mỗi lần áp dụng một operator tại một vị trí trong code, ta có một **mutant** — một phiên bản code gần như giống hệt bản gốc nhưng sai khác một chi tiết nhỏ.

### Bước 2 — Chạy test suite trên từng mutant
Với mỗi mutant, công cụ chạy lại bộ test hiện có (không cần viết test mới) và quan sát kết quả:

- **Killed (bị diệt)**: có ít nhất một test fail → tốt, test đã phát hiện ra "lỗi" giả định.
- **Survived (sống sót)**: tất cả test đều pass → xấu, đây là điểm mù của bộ test.
- **Timeout**: mutant khiến chương trình chạy vô hạn (ví dụ đổi điều kiện dừng vòng lặp) → thường được tính là killed.
- **No coverage**: dòng code chứa mutant chưa từng được test chạy qua → hiển nhiên survived, và cũng là dấu hiệu thiếu test coverage cơ bản.

### Bước 3 — Tính Mutation Score

```
Mutation Score = (Số mutant bị killed) / (Tổng số mutant hợp lệ) × 100%
```

Điểm số này phản ánh trung thực hơn nhiều so với coverage % vì nó đo khả năng **phát hiện sai lệch hành vi**, không chỉ khả năng **chạy qua dòng code**.

## 2. Vì sao mỗi ngôn ngữ dùng một công cụ mutation testing riêng?

Khác với ý tưởng có vẻ trừu tượng của mutation testing, trên thực tế không có công cụ mutation testing nào dùng chung được cho nhiều ngôn ngữ, vì những lý do kỹ thuật sau:

**a) Cách sinh mutant phụ thuộc vào AST/bytecode của từng ngôn ngữ**
Mutation operator phải thao tác trên cây cú pháp trừu tượng (AST) hoặc bytecode đặc thù của ngôn ngữ đó. Parser của JavaScript/TypeScript (Babel) hoàn toàn khác cấu trúc với parser của Python hay bytecode JVM. Một công cụ mutate Python không thể tái sử dụng logic mutate JavaScript.

**b) Cơ chế thực thi và test runner khác nhau**
Mỗi ngôn ngữ có hệ sinh thái test runner riêng (Jest/Mocha/Vitest cho JS, pytest/unittest cho Python, JUnit cho Java...). Công cụ mutation testing cần tích hợp sâu để: (1) biết cách chạy test, (2) biết cách bắt tín hiệu pass/fail, (3) tối ưu để không phải khởi động lại toàn bộ runtime cho mỗi mutant.

**c) Mô hình biên dịch/thực thi khác nhau**
Ngôn ngữ biên dịch tĩnh (Java, C#) có thể mutate ở tầng bytecode sau khi build, tận dụng lại toàn bộ classpath đã compile. Ngôn ngữ thông dịch động (Python, JavaScript) phải mutate mã nguồn hoặc AST trước khi thực thi, và việc "type checking" hay "transpile" (TypeScript) tạo thêm một lớp phức tạp riêng.

**d) Chi phí khởi động (startup cost) khác nhau**
JavaScript trong Node.js hay Python có startup nhanh nhưng lại tốn chi phí transpile/import lại module cho mỗi lần chạy test; JVM có startup chậm nhưng bytecode instrumentation "on-the-fly" lại rất rẻ khi đã trong tiến trình. Mỗi hệ sinh thái cần chiến lược tối ưu hiệu năng khác nhau để mutation testing khả thi trong thực tế.

## 3. StrykerJS — Mutation Testing cho JavaScript/TypeScript

### 3.1 Kiến trúc và cách hoạt động

StrykerJS không mutate trực tiếp lên code gốc. Nó sao chép project vào một thư mục **sandbox**, và mọi thao tác mutate/test đều diễn ra trong đó — đảm bảo mutant không bao giờ lọt vào production.

Quy trình gồm các bước:

1. **Parse & sinh mutant bằng Babel**: Stryker dùng Babel parser để duyệt AST và xác định tất cả các vị trí có thể mutate.

2. **Mutant Schemata (Mutation Switching)** — điểm khác biệt lớn nhất của Stryker so với các công cụ mutation testing "cổ điển":

   Thay vì tạo ra N bản copy code (mỗi mutant một file), Stryker **nhúng tất cả mutant vào cùng một file**, bọc trong điều kiện kiểm tra biến toàn cục `global.__stryker__.activeMutant`:

   ```javascript
   // Code gốc
   function add(a, b) { return a + b; }

   // Sau khi Stryker instrument (rút gọn)
   function add(a, b) {
     return global.__stryker__.activeMutant === 1
       ? a - b          // mutant #1
       : a + b;          // code gốc
   }
   ```

   Nhờ vậy, việc build/bundle/transpile (webpack, tsc...) chỉ cần chạy **một lần duy nhất** cho toàn bộ quá trình, thay vì một lần cho mỗi mutant. Đây là cải thiện hiệu năng lớn vì bước compile TypeScript hay bundle thường tốn thời gian hơn cả bản thân việc chạy test.

3. **Dry run để đo "mutant coverage per test"**: Trước khi test thật sự với mutant, Stryker chạy một lượt test bình thường (dry run) và hook vào `beforeEach` của test framework để ghi nhận: test nào chạm tới dòng code nào. Nhờ dữ liệu này, khi tới lượt kiểm tra một mutant cụ thể, Stryker chỉ cần chạy các test có chạm tới vị trí đó thay vì chạy lại toàn bộ test suite, từ đó giảm đáng kể số lượt test phải chạy.

4. **Mutant run plan**: Dựa trên thông tin coverage-per-test, Stryker lập kế hoạch chạy tối ưu — mutant nào không được test nào chạm tới sẽ được đánh dấu "no coverage" ngay lập tức, khỏi cần chạy test.

5. **Song song hóa**: Stryker chạy nhiều tiến trình test runner song song, tận dụng đa nhân CPU.

6. **Incremental testing**: Với flag `--incremental`, Stryker lưu kết quả cũ vào file cache; ở lần chạy sau, những mutant nằm trong đoạn code không thay đổi sẽ được bỏ qua, biến mutation testing chạy nhanh hơn nhiều.

### 4.2 Hiệu quả thực tế

- **Hỗ trợ đa ngôn ngữ trong hệ sinh thái JS**: JavaScript thuần, TypeScript, và tích hợp với hầu hết test runner phổ biến.
- **Cải thiện tốc độ đáng kể** so với kiến trúc cũ (trước khi có mutation switching), tùy loại project — dự án dùng bundler càng được lợi nhiều vì tránh phải build lại nhiều lần.
- **Linh hoạt phạm vi**: Có thể giới hạn mutate theo file/thư mục (`--mutate`) hoặc chỉ mutate phần code thay đổi so với branch chính (`--since`), rất hợp để tích hợp vào CI/CD trên từng pull request thay vì chạy toàn bộ codebase.

### 4.3 Các bước chạy StrykerJS

```bash
# 1. Cài đặt & khởi tạo cấu hình (cách nhanh nhất, tự hỏi test runner/TS...)
npm init stryker@latest

# 2. Chạy mutation testing với cấu hình mặc định (stryker.config.mjs/json)
npx stryker run

# 3. Một số biến thể hữu ích khi chạy
npx stryker run --mutate "src/billing/**/*.ts"   # chỉ mutate 1 phạm vi cụ thể
npx stryker run --since main                      # chỉ mutate phần code thay đổi so với branch chính
npx stryker run --incremental                     # bật cache, chỉ chạy lại mutant bị ảnh hưởng
npx stryker run --reporters html,clear-text  # chọn định dạng báo cáo

# 4. Xem báo cáo
open reports/mutation/html/index.html
```

## 5. mutmut — Mutation Testing cho Python

### 5.1 Kiến trúc và cách hoạt động

Triết lý thiết kế của mutmut là  đơn giản hóa tối đa để mutation testing trở thành thói quen thường nhật thay vì công việc chuyên biệt chạy một lần rồi bỏ.

1. **Sinh mutant dựa trên AST của Python**: mutmut phân tích cây cú pháp Python và áp dụng các mutation operator để mô phỏng đúng loại lỗi con người dễ mắc, ví dụ: số nguyên `0` → `1`, `5` → `6`; đảo toán tử so sánh; hay với type hint, `x: str = 'foo'` → `x: str = None`.

2. **Không cần chạy toàn bộ AST song song như Stryker**: mutmut đi theo mô hình đơn giản hơn — sinh từng mutant một, áp mutant đó vào file thực tế (có backup), sau đó gọi lệnh test (`pytest` mặc định, nhưng có thể là bất kỳ lệnh nào miễn trả về exit code) để kiểm tra pass/fail. Nhờ chỉ cần exit code, mutmut **tương thích với mọi test runner** mà không cần viết plugin riêng cho từng framework — đơn giản nhưng đổi lại kém tinh vi hơn Stryker ở khoản chọn lọc test cần chạy.

3. **Tận dụng dữ liệu coverage để cắt giảm phạm vi**: mutmut có thể đọc dữ liệu từ `coverage.py`; những dòng code chưa từng được test chạy qua sẽ bị loại khỏi việc sinh mutant ngay từ đầu — giảm số lượng mutant "chắc chắn survived" một cách vô nghĩa.

4. **Cache kết quả (`.mutmut-cache`)**: Đây là cơ chế cốt lõi giúp mutmut chạy "incremental" — mutmut nhớ những mutant đã kiểm tra và kết quả của chúng. Nếu source code hoặc cấu hình ảnh hưởng tới mutant đó không đổi, lần chạy sau sẽ bỏ qua, chỉ chạy lại các mutant mới hoặc bị ảnh hưởng bởi thay đổi. 

5. **Có thể dừng và tiếp tục bất cứ lúc nào**: vì mỗi mutant được kiểm tra độc lập và ghi nhận ngay vào cache, bạn có thể ngắt quá trình `mutmut run` giữa chừng và chạy lại sau — nó sẽ tiếp tục từ chỗ dừng thay vì làm lại từ đầu.

6. **Loại trừ mutant thủ công**: Dùng comment `# pragma: no mutate` (cho một dòng), hoặc `# pragma: no mutate block` (cho cả khối lệnh) để loại trừ những đoạn code không cần/không nên mutate (ví dụ logging, code phòng thủ khó test).

### 5.2 Hiệu quả thực tế

- **Rất dễ tích hợp**: chỉ cần cài `pip install mutmut` và chạy `mutmut run`, hầu như không cần cấu hình phức tạp cho project vừa và nhỏ.
- **Tương thích rộng**: vì chỉ cần exit code, mutmut hoạt động được với bất kỳ test runner nào (pytest, unittest, hoặc custom script) — không bị khóa cứng vào một framework như một số công cụ khác.
- **Giới hạn về nền tảng**: mutmut yêu cầu hệ thống có hỗ trợ `fork` (Unix-style), nên trên Windows phải chạy trong WSL.
- **Thời gian chạy lâu**: Vì không có cơ chế "mutation switching" hay "coverage-per-test" tinh vi như StrykerJS, với dự án Python rất lớn, mutmut có thể chậm hơn tương đối nếu không tận dụng cache/coverage filtering — chi phí chủ yếu nằm ở việc phải khởi động lại quá trình test (thường là cả tiến trình Python + import lại module) cho mỗi mutant, thay vì switch một biến toàn cục như StrykerJS.

### 5.3 Các bước chạy mutmut

```bash
# 1. Cài đặt
pip install mutmut

# 2. Chạy mutation testing (mặc định tự tìm code trong project + thư mục tests/)
mutmut run

# Có thể giới hạn phạm vi mutate
mutmut run --paths-to-mutate=src/calculator.py

# 3. Xem tổng quan kết quả (killed/survived/timeout...)
mutmut results

# 4. Xem chi tiết một mutant cụ thể (ví dụ mutant #3) để biết chính xác thay đổi gì
mutmut show 3

# 5. (Tùy chọn) Áp mutant đó thẳng vào code để debug tại sao nó sống sót
mutmut apply 3

# 6. Sinh báo cáo HTML để duyệt trực quan
mutmut html
```

