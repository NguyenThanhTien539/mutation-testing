# Đo Test Effectiveness bằng Code Coverage: Nguyên Lý và Hai Công Cụ Tiêu Biểu (Istanbul & Coverage.py)

## 1. Nguyên lý hoạt động chung: Instrumentation

Để biết dòng/nhánh nào được thực thi, công cụ coverage phải **cấy các bộ đếm (counter)** vào đâu đó trong quá trình chạy code. Có ba cách tiếp cận chính:

### a) Source-level instrumentation (chèn counter vào mã nguồn)
Công cụ parse mã nguồn thành AST, chèn thêm lệnh tăng biến đếm vào từng statement/branch, rồi sinh lại mã nguồn đã "instrumented" để chạy thay cho bản gốc.

```javascript
// Trước
function greet(name) {
  if (name) { return `Hello, ${name}!`; }
  return 'Hello, stranger!';
}

// Sau khi instrument (rút gọn ý tưởng)
function greet(name) {
  cov.f[0]++;              // đếm hàm được gọi
  cov.s[0]++;               // đếm statement
  if (name) {
    cov.b[0][0]++;          // đếm nhánh true
    return `Hello, ${name}!`;
  } else {
    cov.b[0][1]++;          // đếm nhánh false
  }
  return 'Hello, stranger!';
}
```
Ưu điểm: chính xác tuyệt đối với mã nguồn gốc, không phụ thuộc runtime. Nhược điểm: tốn thời gian parse + tăng kích thước code + overhead runtime.

### b) Bytecode-level instrumentation (chèn probe vào bytecode đã biên dịch)
Áp dụng cho ngôn ngữ biên dịch ra bytecode trung gian (Java → JVM bytecode). Công cụ sửa trực tiếp bytecode để chèn các "probe" (thường chỉ là một mảng boolean được set thành true khi đoạn code chạy qua), không cần động đến mã nguồn `.java`.

### c) Engine-native instrumentation (dùng cơ chế theo dõi có sẵn của runtime)
Một số engine hiện đại (V8 trong Node.js/Chrome) có sẵn khả năng ghi lại "byte range nào của script đã thực thi" ở tầng engine, không cần transform code. Công cụ coverage chỉ cần bật cờ và đọc dữ liệu ra sau khi chạy xong, rồi map ngược về file nguồn qua source map. Cách này nhanh hơn nhưng kém chính xác hơn với code đã bundle/transpile phức tạp (JSX, TypeScript...).

Sau khi thu thập xong dữ liệu thô, công cụ sẽ **tổng hợp và xuất báo cáo** (HTML, LCOV, Cobertura XML, JSON...) để hiển thị phần trăm coverage theo file/thư mục/toàn dự án, và có thể tích hợp với CI để fail build nếu coverage dưới ngưỡng quy định.

## 2. Istanbul — Coverage cho JavaScript/TypeScript

### 2.1 Cách hoạt động

Istanbul là công cụ **source-level instrumentation** cho JavaScript. Quy trình gồm:

1. **Parse mã nguồn thành AST**: Istanbul (qua thư viện lõi `istanbul-lib-instrument`) hoặc plugin Babel (`babel-plugin-istanbul`) duyệt AST để xác định vị trí của mọi statement, function, và branch (if/else, ternary, switch, toán tử logic ngắn mạch).

2. **Chèn bộ đếm vào AST rồi sinh lại code**: Mỗi statement được gắn `cov_xxx.s[N]++`, mỗi hàm gắn `cov_xxx.f[N]++`, mỗi nhánh gắn `cov_xxx.b[N][0/1]++`. Bản đồ giữa các chỉ số N và vị trí dòng/cột trong mã nguồn gốc (kể cả khi qua Babel/TypeScript, nhờ source map) được lưu lại trong một *coverage map*.

3. **Runtime ghi dữ liệu vào biến toàn cục**: Khi test chạy (qua Jest, Mocha, AVA...), code instrumented tự tăng các bộ đếm này trong bộ nhớ (`global.__coverage__` khi chạy Node, hoặc `window.__coverage__` khi chạy trên trình duyệt).

4. **`nyc` — CLI điều phối**: `nyc` là công cụ dòng lệnh phổ biến nhất để chạy Istanbul trong thực tế. Nó chèn instrumentation vào mọi file được `require()` trong lúc test chạy, thu thập dữ liệu `__coverage__` sau khi test kết thúc (kể cả từ tiến trình con nếu cấu hình), rồi tổng hợp thành báo cáo. `nyc` mặc định cache các file đã instrument để tránh phải instrument lại nhiều lần, giúp tăng tốc các lần chạy sau.

5. **Sinh báo cáo đa định dạng**: text summary trên terminal, HTML để duyệt trực quan từng dòng, LCOV để tích hợp với các dịch vụ như Codecov/Coveralls, JSON để xử lý tiếp bằng công cụ khác.

### 2.2 Istanbul so với coverage native của V8

Đây là điểm đáng chú ý trong hệ sinh thái JS hiện đại: kể từ khi Node.js hỗ trợ V8 coverage built-in, các công cụ như `c8` xuất hiện, đo coverage trực tiếp ở tầng engine mà không cần transform code — nhanh hơn Istanbul đáng kể nhưng làm việc trên code đã bundle nên phải dựa vào source map để đoán ngược vị trí gốc, dễ sai lệch với các cấu trúc JSX phức tạp hoặc khi dùng SWC thay vì Babel. Istanbul, vì instrument thẳng trên mã nguồn gốc trước khi transform, giữ được độ chính xác cao hơn cho branch coverage — đây là lý do nhiều dự án coi trọng độ chính xác vẫn chọn Istanbul dù chậm hơn.

### 2.3 Hiệu quả thực tế

- Độ chính xác cao: vì mọi counter được cấy trực tiếp vào cấu trúc AST gốc, Istanbul cho kết quả branch coverage rất đáng tin cậy, kể cả với logic lồng nhau phức tạp.
- Hệ sinh thái trưởng thành, tương thích rộng: hoạt động tốt với hầu hết test framework JS, và định dạng JSON coverage của Istanbul đã trở thành chuẩn thực tế — nhiều công cụ khác xuất báo cáo theo đúng schema Istanbul để tương thích ngược.
- Chi phí hiệu năng: vì phải parse + biến đổi AST + code chạy chậm hơn do có thêm lệnh đếm ở mọi statement, Istanbul chậm hơn đáng kể so với coverage engine-native (V8/c8) — có báo cáo thực tế cho thấy chênh lệch nhiều lần tùy quy mô dự án.

### 2.4 Các bước chạy Istanbul (qua `nyc`)

```bash
# 1. Cài đặt nyc (CLI phổ biến nhất để chạy Istanbul)
npm install --save-dev nyc

# 2. Chạy test suite kèm đo coverage (ví dụ với Mocha)
npx nyc mocha
# Hoặc gọi qua script npm test đã khai báo sẵn
npx nyc npm test

# 3. Xem báo cáo dạng text ngay trên terminal (mặc định khi chạy xong)
npx nyc report

# 4. Xuất báo cáo ở định dạng khác 
npx nyc report --reporter=html

# 5. Kiểm tra coverage có đạt ngưỡng tối thiểu không (fail build nếu không đạt)
npx nyc check-coverage --lines 90 --branches 85 --functions 90

```

Với Jest và Vitest, Istanbul thường được dùng gián tiếp — chỉ cần bật cờ `--coverage` và chọn `coverageProvider: 'babel'` (Jest) hoặc `provider: 'istanbul'` (Vitest) trong file cấu hình, không cần gọi `nyc` thủ công.

## 3. Coverage.py — Coverage cho Python

### 3.1 Cách hoạt động

Khác hẳn với Istanbul, Coverage.py không hề chèn thêm dòng code hay counter nào vào mã nguồn. Thay vào đó, nó khai thác chính cơ chế theo dõi thực thi có sẵn của interpreter Python — nói cách khác, đây là kiểu engine-native instrumentation (giống cách V8 coverage hoạt động với JavaScript), chứ không phải source-level instrumentation như Istanbul.

Coverage.py hiện có 3 cơ chế  khác nhau, có thể chọn tùy phiên bản Python:

**a) `ctrace` — trace function viết bằng C (mặc định, nhanh nhất)**
Python có sẵn API `sys.settrace()`, cho phép đăng ký một hàm callback được interpreter gọi lại ở mỗi dòng code được thực thi. Coverage.py đăng ký một trace function để nhận sự kiện này và ghi lại "file + số dòng" tương ứng. Vì gọi một hàm Python thuần cho mỗi dòng sẽ rất chậm, Coverage.py triển khai phiên bản trace function bằng C (module mở rộng `tracer`) để giảm overhead xuống mức chấp nhận được.

**b) `pytrace` — trace function viết bằng Python (chậm hơn, để tương thích)**
Cùng cơ chế `sys.settrace()` nhưng cài đặt thuần Python — dùng khi không có sẵn bản C-extension đã biên dịch cho nền tảng/phiên bản Python cụ thể, đổi lại chậm hơn đáng kể.

**c) `sysmon` — dùng `sys.monitoring` (Python 3.12+)**
Từ Python 3.12, CPython bổ sung API `sys.monitoring` — một cơ chế giám sát sự kiện thực thi hiệu quả hơn nhiều so với `sys.settrace()` truyền thống (vốn được thiết kế ban đầu cho debugger nên có overhead cao). Coverage.py tận dụng API mới này làm core `sysmon`, giúp giảm đáng kể chi phí runtime so với `ctrace`/`pytrace` trên các phiên bản Python mới.

### 3.2 Lưu trữ dữ liệu và hỗ trợ file không phải Python

Trong lúc thu thập, Coverage.py liên tục ghi dữ liệu ra một file (**mặc định `.coverage`**) — đây thực chất là một **cơ sở dữ liệu SQLite**, không phải file text đơn giản. Việc dùng SQLite giúp Coverage.py dễ dàng gộp (combine) dữ liệu từ nhiều tiến trình/nhiều lần chạy (ví dụ chạy test song song bằng `pytest-xdist`, hoặc gộp coverage của nhiều môi trường tox khác nhau) thông qua lệnh `coverage combine`.

Một tính năng đáng chú ý là **file tracer plugin**: vì Coverage.py về bản chất theo dõi việc thực thi file `.py`, nó có cơ chế mở rộng cho phép một plugin "nhận diện" khi nào việc thực thi Python thực chất đang chạy hộ cho một file không phải Python — ví dụ template Django HTML được compile ngầm thành Python bytecode lúc render. Plugin sẽ ánh xạ ngược kết quả thực thi đó về đúng dòng trong file `.html` gốc, giúp coverage phản ánh đúng góc nhìn của lập trình viên thay vì chỉ dừng ở code Python sinh ra ngầm.

### 3.3 Context động

Coverage.py hỗ trợ gắn nhãn **"dynamic context"** cho dữ liệu thu thập được — ví dụ gắn nhãn theo tên test đang chạy. Nhờ vậy có thể trả lời được câu hỏi "dòng code này được **test nào** chạy qua" chứ không chỉ "có được chạy qua hay không" — hữu ích khi cần drill-down xem test nào chịu trách nhiệm cho phần coverage nào.

### 3.4 Hiệu quả thực tế

- Không cần build pipeline riêng: vì không transform mã nguồn, Coverage.py hoạt động "trong suốt" với mọi cách chạy Python — không có bước biên dịch/transpile trung gian nào cần lo lắng như Istanbul phải lo với Babel/TypeScript.
- Overhead phụ thuộc nhiều vào core được chọn: `ctrace` (C extension) thường đủ nhanh cho hầu hết dự án, nhưng vẫn chậm hơn code không đo coverage vì phải gọi callback ở mỗi dòng; core `sysmon` (Python 3.12+) giảm đáng kể overhead này nhờ API giám sát mới hiệu quả hơn so với cơ chế `sys.settrace()` cũ vốn được thiết kế cho mục đích debug.
- Chính xác đến từng dòng lệnh Python: vì bám sát interpreter thật, Coverage.py phản ánh đúng những gì đã chạy — không có vấn đề "map ngược qua source map" như một số công cụ dựa trên bytecode/engine của ngôn ngữ khác biên dịch/transpile nhiều tầng.

### 3.5 Các bước chạy Coverage.py

```bash
# 1. Cài đặt
pip install coverage
# Hoặc cài kèm plugin pytest (khuyến nghị nếu dùng pytest)
pip install pytest-cov

# 2a. Chạy trực tiếp bằng Coverage.py
coverage run -m pytest

# 2b. Hoặc chạy qua plugin pytest-cov (gộp luôn vào 1 lệnh test)
pytest --cov=src --cov-report=term-missing

# 3. Xem báo cáo dạng text trên terminal (chỉ ra cả những dòng chưa được test)
coverage report -m

# 4. Xuất báo cáo HTML để duyệt trực quan từng dòng
coverage html
# Mở file htmlcov/index.html trong trình duyệt

# 5. Xuất báo cáo XML 
coverage xml

# 6. Bật đo branch coverage 
coverage run --branch -m pytest
```

