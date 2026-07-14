# Khảo sát công cụ: Infection PHP và Major

## 1. Mục tiêu

Nghiên cứu bối cảnh, mục đích và cách sử dụng Infection PHP và Major cho seminar Mutation Testing & Test Effectiveness. Đánh giá cách các công cụ này đo lường mức độ bao phủ của bộ kiểm thử, từ đó làm cơ sở đánh giá hiệu quả của test trước khi áp dụng các kỹ thuật nâng cao như Mutation Testing.

## 2. Infection PHP

### 2.1 Tổng quan công cụ

Infection là một thư viện kiểm thử đột biến (mutation testing) cho PHP, dựa trên các đột biến cây cú pháp trừu tượng (AST - Abstract Syntax Tree). Nó hoạt động như một công cụ dòng lệnh (CLI) và có thể được thực thi từ thư mục gốc của dự án.

### 2.2 Mục đích chính

Là công cụ kiểm thử đột biến đơn giản, dễ cài đặt, thân thiện với người mới bắt đầu, sử dụng các đột biến AST kết hợp với tích hợp phân tích tĩnh (Static Analysis Integration) để tối đa hóa hiệu quả kiểm thử trên các framework như PHPUnit, PhpSpec, Codeception và Testo.

### 2.3 Ngôn ngữ/Nền tảng hỗ trợ

Infection hiện hỗ trợ các framework kiểm thử PHPUnit, PhpSpec, Codeception và Testo; yêu cầu PHP 8.3+ và đã cài đặt Xdebug/phpdbg/pcov.

### 2.4 Cách công cụ hoạt động

Tóm lại, công cụ này:

1. Chạy bộ kiểm thử để đảm bảo tất cả các test đều vượt qua.
2. Đột biến mã nguồn với một tập hợp các mutator (toán tử đột biến) được xác định trước.
3. Với mỗi Mutant (mã đã được thay đổi), nó chạy các test bao phủ dòng mã đó.
4. Phân tích xem các test có bị lỗi hay không.
5. Thu thập kết quả của các Mutant bị tiêu diệt (killed), thoát (escaped), lỗi và hết thời gian (timeouts).

### 2.5 Tính năng chính

- Thực hiện kiểm thử đột biến sử dụng các đột biến AST.
- Tích hợp phân tích tĩnh (Static Analysis Integration) đầy đủ để giúp cải thiện hiệu quả kiểm thử đột biến bằng cách phát hiện các lỗi logic mà test có thể bỏ sót.

### 2.6 Trường hợp sử dụng phổ biến

- Tích hợp kiểm thử đột biến với PHP, Xdebug, phpdbg, hoặc pcov.
- Kiểm thử đột biến đơn giản và thân thiện cho các dự án đã thực hiện đầy đủ việc tích hợp phân tích tĩnh.

### 2.7 Điểm mạnh

- Sự khác biệt lớn nhất và tốt nhất là Infection sử dụng AST để đột biến mã nguồn.
- Dễ dàng bảo trì mã nguồn hơn.
- Dễ dàng viết các Mutator mới hơn.
- Dễ dàng xử lý các kết quả dương tính giả (false-positives) và các trường hợp biên, ví dụ như quyết định khi nào nên hoặc không nên thực hiện đột biến trong các tình huống khó.
- Hỗ trợ nhiều loại cấu hình và đột biến, cho phép người dùng lựa chọn và áp dụng cho dự án của họ.

### 2.8 Giới hạn

- Infection yêu cầu phiên bản PHP mới nhất và phải bật Xdebug, phpdbg hoặc pcov.
- Các đột biến phải xảy ra khi CodeCoverage đã bắt đầu, nếu không chúng sẽ không được báo cáo.

### 2.9 Chi phí/Giấy phép

- Chi phí: Miễn phí.
- Giấy phép: Được phát hành dưới giấy phép BSD-3-Clause.

### 2.10 Hỗ trợ AI, nếu có

Infection PHP là một công cụ kiểm thử truyền thống nên không được tích hợp AI ở mức cơ bản.

### 2.12 Tài liệu tham khảo

- Tài liệu đầy đủ từ tác giả: [https://infection.github.io/](https://infection.github.io/)

## 3. Major

### 3.1 Tổng quan công cụ

Major là một framework phân tích đột biến (mutation analysis) linh hoạt và hiệu quả. Công cụ này cung cấp một plugin đột biến (mutator) cho trình biên dịch Java `javac` nhằm duyệt qua và dịch cây cú pháp trừu tượng (AST). Tất cả các đột biến (mutants) được nhúng trực tiếp vào AST và được biên dịch thành byte-code.

### 3.2 Mục đích chính

Major hỗ trợ việc tạo và nhúng các đột biến trong quá trình biên dịch. Công cụ này dùng để tính toán tỷ lệ phát hiện đột biến và tập hợp các đột biến còn sống (live mutants) cho một tập hợp các bài kiểm thử nhất định. Ngoài ra, nó cũng tính toán một ma trận phát hiện kiểm thử đột biến (mutant-test detection matrix) hoàn chỉnh.

### 3.3 Ngôn ngữ/Nền tảng hỗ trợ

Major yêu cầu sử dụng trình biên dịch Java-8 (có thể xác minh bằng lệnh `javac -version`). Phân tích đột biến có thể được thực thi thông qua Apache Ant hoặc Major độc lập (standalone). Quá trình chạy phân tích kiểm thử được hỗ trợ qua cấu hình của JUnit.

### 3.4 Cách công cụ hoạt động

1. Trình biên dịch MML của Major (`mmlc`) xác thực một tệp mml và biên dịch nó thành dạng biểu diễn nhị phân.
2. Mutator của Major sử dụng tệp mml đã biên dịch để cấu hình quá trình tạo đột biến.
3. Các đột biến được nhúng vào AST và biên dịch thành byte-code.
4. Công cụ phân tích (analyzer) nhận tập hợp các đột biến đã tạo và thực thi một bộ kiểm thử (test suite) trên chúng.
5. Kết quả phân tích được xuất ra các tệp như `summary.csv` và `details.csv` để báo cáo tổng quan, hoặc `killed.csv` để ghi nhận lý do một đột biến bị phát hiện (lỗi assertion, ngoại lệ, hoặc timeout) hay còn sống.

### 3.5 Tính năng chính

- Tạo và nhúng các đột biến ngay trong quá trình biên dịch.
- Hỗ trợ xuất các đột biến mã nguồn.
- Loại bỏ (suppressing) các đột biến tương đương.
- Cung cấp Mml (Major Mutation Language): một ngôn ngữ miền cụ thể (DSL) để tùy chỉnh việc tạo đột biến.
- Công cụ phân tích (Analyzer) xác định hiệu quả các đột biến còn sống, tỷ lệ phát hiện đột biến hoặc ma trận kiểm thử đột biến đầy đủ.

### 3.6 Trường hợp sử dụng phổ biến

- Tùy chỉnh việc tạo đột biến bằng tệp mml.
- Tạo các đột biến bằng mutator của Major.
- Phân tích các đột biến bằng analyzer mặc định của Major.
- Gọi mutator của Major từ một mục tiêu biên dịch (compile target) của Apache Ant.

### 3.7 Điểm mạnh

- Là một framework phân tích đột biến linh hoạt và hiệu quả.
- Các đột biến riêng lẻ có thể được kích hoạt (enabled) trong thời gian chạy (runtime) mà không cần phải biên dịch lại.
- Ngôn ngữ mml hỗ trợ cấu hình cực kỳ chi tiết cho quá trình tạo đột biến (ví dụ: thay thế toán tử, định nghĩa các loại câu lệnh bị xóa, v.v.).
- Lớp cấu hình thời gian chạy (run-time configuration class) không cần thiết phải có trên classpath trong quá trình tạo đột biến, vì mutator sẽ tự tạo các node AST dựa trên interface.

### 3.8 Giới hạn

- Tính năng xuất các đột biến thành các tệp mã nguồn riêng lẻ bị vô hiệu hóa (disabled) theo mặc định.
  _(Lưu ý: Tài liệu được cung cấp không đề cập rõ các giới hạn khác của hệ thống)._

### 3.9 Chi phí/Giấy phép

_(Không có thông tin trong tài liệu được cung cấp)._

### 3.10 Hỗ trợ AI, nếu có

_(Không có thông tin trong tài liệu được cung cấp)._

### 3.11 Tiềm năng demo

Gói phát hành của Major cung cấp sẵn thư mục `example` chứa các ví dụ thực hành (như chương trình `triangle` và tệp cấu hình mml) để thực hiện phân tích đột biến bằng Apache Ant hoặc standalone. Người dùng có thể thực thi tập lệnh `runAll.sh` trong thư mục ví dụ để chạy tất cả các demo.

### 3.12 Tài liệu tham khảo

- Thư mục `doc` đi kèm trong gói cài đặt chứa hướng dẫn sử dụng (manual) của phiên bản hiện tại (tệp `major.html`).
