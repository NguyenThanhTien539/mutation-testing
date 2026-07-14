# So sánh 11 công cụ Mutation Testing & Code Coverage

---

## 1. Infection PHP

**Ngôn ngữ:** PHP

**Pricing:** Miễn phí hoàn toàn (BSD-3-Clause)

**Strengths:**

- Sử dụng AST (Abstract Syntax Tree) để đột biến mã nguồn, giúp đột biến chính xác và dễ bảo trì
- Dễ viết các Mutator mới
- Xử lý tốt false-positives và các trường hợp biên
- Tích hợp phân tích tĩnh (Static Analysis Integration)
- Hỗ trợ nhiều framework: PHPUnit, PhpSpec, Codeception, Testo

**Weaknesses:**

- Yêu cầu PHP 8.3+ và phải bật Xdebug/phpdbg/pcov
- Các đột biến phải xảy ra khi CodeCoverage đã bắt đầu, nếu không sẽ không được báo cáo
- Không hỗ trợ multiprocessing trên Windows

**AI Support:** Không có AI tích hợp sẵn. Không có thông tin về ứng dụng phối hợp AI.

---

## 2. Major

**Ngôn ngữ:** Java

**Pricing:** Miễn phí

**Strengths:**

- Framework phân tích đột biến linh hoạt và hiệu quả
- Các đột biến có thể được kích hoạt trong thời gian chạy mà không cần biên dịch lại
- Ngôn ngữ MML (Major Mutation Language) hỗ trợ cấu hình cực kỳ chi tiết cho quá trình tạo đột biến
- Tính toán mutant-test detection matrix hoàn chỉnh

**Weaknesses:**

- Tính năng xuất đột biến thành tệp mã nguồn riêng lẻ bị vô hiệu hóa theo mặc định
- Yêu cầu Java-8 compiler
- Ít thông tin tài liệu so với các tool khác
- Cộng đồng hỗ trợ hạn chế hơn

**AI Support:** Không có AI tích hợp sẵn. Chỉ có thể dùng AI bên ngoài để hỗ trợ.

---

## 3. Istanbul/nyc

**Ngôn ngữ:** JavaScript, TypeScript

**Pricing:** Miễn phí hoàn toàn (ISC License)

**Strengths:**

- Cài đặt và sử dụng cực kỳ đơn giản (chỉ cần thêm `nyc` trước lệnh test)
- Báo cáo HTML trực quan, chi tiết
- Tiêu chuẩn công nghiệp (de-facto standard) cho JavaScript
- Tương thích tốt với hệ thống plugin (babel-plugin-istanbul)
- Đo lường 4 chỉ số: Statements, Branches, Functions, Lines

**Weaknesses:**

- Quá trình instrumentation có thể làm tăng thời gian thực thi test suite ở dự án lớn
- Cấu hình source-map phức tạp trong Monorepo hoặc dự án build nhiều bước
- Không phải mutation testing tool - chỉ đo code coverage

**AI Support:** Không tích hợp AI trực tiếp. Dữ liệu đầu ra (JSON/LCOV) thường được dùng làm đầu vào cho các nền tảng AI như SonarQube, Codecov để AI gợi ý viết test tự động.

---

## 4. JaCoCo

**Ngôn ngữ:** Java

**Pricing:** Miễn phí hoàn toàn (Eclipse Public License - EPL)

**Strengths:**

- Không cần sửa đổi mã nguồn gốc (làm việc trực tiếp dưới mức bytecode)
- Tích hợp chuẩn hóa với Maven/Gradle chỉ với vài dòng XML
- Nhẹ, nhanh, overhead cực thấp
- Đo lường chi tiết: Instructions, Branches, Lines, Cyclomatic Complexity, Methods, Classes
- Báo cáo trực quan bằng mã màu sinh động
- Coverage Gate (`check` goal) để thiết lập ngưỡng coverage
- Gộp báo cáo cho dự án đa module

**Weaknesses:**

- Kết quả ở cấp bytecode có thể khác biệt so với source gốc
- On-the-fly agent có thể bị xung đột với framework tự động chỉnh sửa bytecode
- Coverage cao tạo ra "ảo giác an toàn" - không xác minh assertion có đúng không
- Không phải mutation testing tool - chỉ đo code coverage

**AI Support:** Không tích hợp AI trực tiếp. Định dạng XML chuẩn mực là đầu vào quan trọng cho các AI Testing Agent (KaneAI, QA agents) để tự động sinh test case bổ sung.

---

## 5. Mutmut

**Ngôn ngữ:** Python

**Pricing:** Miễn phí hoàn toàn (BSD 3-Clause License)

**Strengths:**

- Cực kỳ dễ sử dụng, cài đặt nhanh qua `pip install mutmut`, cấu hình tối giản
- Tốc độ nhanh nhờ bộ nhớ đệm SQLite và coverage-guided mutation
- Kiểm thử tăng dần (incremental) - chỉ chạy lại mutant liên quan đến code mới sửa
- `mutmut browse` - dashboard text cho phép duyệt qua từng mutant
- Khả năng áp dụng đột biến lên ổ đĩa để debug thủ công
- Báo cáo HTML trực quan

**Weaknesses:**

- Chạy tuần tự đơn tiến trình theo mặc định, chậm ở dự án lớn
- Vẫn tạo ra equivalent mutants
- Hỗ trợ multiprocessing trên Windows gặp vấn đề
- Không phải framework phân tán

**AI Support:** Không tích hợp AI trực tiếp. Kết quả từ `.mutmut-cache` hoặc báo cáo HTML phù hợp làm prompt cho AI coding assistants (Claude, ChatGPT, Cursor) để giải thích mutant sống sót, sinh test bổ sung, phân tích equivalent mutants.

---

## 6. Cosmic Ray

**Ngôn ngữ:** Python

**Pricing:** Miễn phí hoàn toàn (BSD 2-Clause License)

**Strengths:**

- Khả năng mở rộng cực tốt với kiến trúc phân tán (Celery, HTTP distributor)
- Quản lý phiên làm việc bền vững qua SQLite - chạy tác vụ dài ngày không sợ mất dữ liệu
- Dừng và tiếp tục bất kỳ lúc nào (pause/resume)
- Hệ thống toán tử đột biến phong phú
- Khả năng mở rộng cao qua plugin
- Độ chính xác cao với parser `parso`

**Weaknesses:**

- Độ phức tạp cấu hình cao - nhiều lệnh tuần tự (new-config → init → baseline → exec)
- Chi phí thiết lập phân tán lớn (cần Celery, Redis/RabbitMQ)
- Tốc độ chạy đơn nhân chậm hơn Mutmut
- Cộng đồng hỗ trợ kém năng động hơn Mutmut
- Rào cản cho người mới bắt đầu

**AI Support:** Không tích hợp AI trực tiếp. Cấu trúc SQLite chi tiết có thể được AI đọc để phân tích thống kê và đề xuất viết code/test hiệu quả hơn.

---

## 7. StrykerJS

**Ngôn ngữ:** JavaScript, TypeScript, Node.js, React, Angular, Vue, Svelte

**Pricing:** Miễn phí hoàn toàn (Apache 2.0 License)

**Strengths:**

- Đánh giá test suite sâu hơn code coverage - kiểm tra test có phát hiện lỗi logic không
- Hỗ trợ nhiều framework và test runner (Jest, Mocha, Jasmine, Karma, Vitest)
- Báo cáo rõ ràng, trực quan với nhiều dạng report (HTML, dashboard)
- Giúp phát hiện test yếu, thiếu assertion hoặc thiếu boundary case
- Dễ demo trực quan

**Weaknesses:**

- Chạy chậm hơn test thông thường
- Cần test suite ban đầu ổn định
- Có thể sinh ra equivalent mutants
- Với project lớn, cần giới hạn phạm vi mutate
- Người dùng cần hiểu report để phân biệt mutant sống do test yếu hay equivalent mutant

**AI Support:** Không tích hợp AI trực tiếp. AI có thể hỗ trợ: giải thích mutation report, gợi ý test case để kill survived mutants, phân tích vì sao mutant survived, viết thêm boundary/negative test.

---

## 8. Jest Coverage

**Ngôn ngữ:** JavaScript, TypeScript, Node.js, React

**Pricing:** Miễn phí hoàn toàn (MIT License)

**Strengths:**

- Dễ bật và dễ chạy (`jest --coverage`)
- Tích hợp trực tiếp trong Jest
- Report dễ đọc
- Hỗ trợ coverage threshold để kiểm soát chất lượng
- Có thể dùng nhanh trong demo

**Weaknesses:**

- Chỉ đo việc code có được chạy qua hay không
- Không kiểm tra assertion có đúng và đủ mạnh không
- Không kiểm tra test có phát hiện lỗi logic không
- Không phải mutation testing tool
- Coverage cao không đảm bảo test chất lượng cao

**AI Support:** Không có tính năng AI tích hợp trực tiếp. AI có thể hỗ trợ: đọc coverage report, gợi ý test case cho file có coverage thấp, gợi ý branch/edge case cần test.

---

## 9. Stryker.NET

**Ngôn ngữ:** C#, .NET Core, .NET Framework

**Pricing:** Miễn phí hoàn toàn (open-source)

**Strengths:**

- Native với .NET/C# ecosystem
- Chạy đơn giản bằng `dotnet stryker`
- Report trực quan với HTML report
- Có nhiều mutation levels (Basic, Standard, Advanced, Complete)
- Thresholds để dùng như quality gate
- `since` và baseline giúp giảm thời gian chạy trên project lớn
- Dễ trình bày trong demo

**Weaknesses:**

- Chạy lâu với solution lớn
- Cấu hình nhiều test projects có thể phức tạp
- Một số behavior đặc thù của xUnit/NUnit theories có thể ảnh hưởng
- Microsoft Testing Platform runner vẫn ở preview
- Có thể xuất hiện equivalent mutants

**AI Support:** Không tích hợp AI trực tiếp. AI có thể hỗ trợ: phân tích survived mutants, gợi ý missing assertions, đề xuất thêm boundary test cases, tóm tắt mutation report, giải thích vì sao mutant survived.

---

## 10. PIT (Pitest)

**Ngôn ngữ:** Java, JVM

**Pricing:** Miễn phí (open-source). PIT core miễn phí; các phần nâng cao như Arcmutate có thể thuộc dạng commercial/pro.

**Strengths:**

- Mature và phổ biến trong Java/JVM ecosystem
- Tích hợp Maven tốt qua `pitest-maven`
- Bytecode mutation giúp chạy nhanh và phù hợp với build pipeline
- Coverage-guided test selection
- Thresholds để fail build nếu score thấp
- Incremental analysis cho codebase lớn
- Hệ thống mutator phong phú (CONDITIONALS_BOUNDARY, MATH, INCREMENTS, VOID_METHOD_CALLS...)

**Weaknesses:**

- Bytecode mutation khó giải thích hơn source-level mutation
- Report map bytecode-level mutation về source line đôi khi không trực quan
- JUnit 5 cần plugin, không hỗ trợ trực tiếp out of the box
- Static initializers và enum-related code có thể khó mutate
- Integration-heavy tests có thể làm runtime dài
- Có thể xuất hiện equivalent mutants

**AI Support:** Không tích hợp AI trực tiếp. AI có thể hỗ trợ: tóm tắt mutation report, phân loại survived mutants theo nguyên nhân, gợi ý JUnit test cases để kill mutants, giải thích bytecode-level mutation bằng source-level terms, đề xuất boundary tests.

---

## 11. Coverage.py

**Ngôn ngữ:** Python

**Pricing:** Miễn phí hoàn toàn (Apache License 2.0)

**Strengths:**

- Tiêu chuẩn công nghiệp (de-facto standard) cho hệ sinh thái Python, duy trì liên tục hơn 20 năm
- Tích hợp liền mạch với `pytest` qua `pytest-cov`
- Hỗ trợ cả Statement và Branch coverage
- Report HTML trực quan, có highlight từng dòng
- Từ Python 3.12, overhead giảm mạnh nhờ `sys.monitoring` (PEP 669)
- Là nền tảng dữ liệu để Mutmut chạy coverage-guided mutation hiệu quả hơn

**Weaknesses:**

- Chỉ đo dòng code có chạy qua hay không, không xác minh assertion có đúng logic
- Branch coverage không bật mặc định, dễ gây ngộ nhận nếu quên cấu hình `branch = True`
- Chạy đa tiến trình cần thêm bước `coverage combine` thủ công, dễ bị bỏ sót
- Không phải mutation testing tool - chỉ đo code coverage

**AI Support:** Không có tính năng AI tích hợp trực tiếp. Dữ liệu XML/JSON có thể làm đầu vào cho SonarQube/Codecov; dữ liệu `.coverage` cũng chính là thứ Mutmut đọc để tối ưu phạm vi mutate tự động.
