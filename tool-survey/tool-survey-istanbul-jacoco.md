# Khảo sát công cụ: Istanbul/nyc và JaCoCo

## 1. Mục tiêu

Nghiên cứu bối cảnh, mục đích và cách sử dụng Istanbul/nyc (cho hệ sinh thái JavaScript/TypeScript) và JaCoCo (cho hệ sinh thái Java) phục vụ cho seminar "Mutation Testing & Test Effectiveness". Đánh giá cách các công cụ này đo lường mức độ bao phủ của bộ kiểm thử, từ đó làm cơ sở đánh giá hiệu quả của test trước khi áp dụng các kỹ thuật nâng cao như Mutation Testing.

## 2. Istanbul/nyc

### 2.1 Tổng quan công cụ

Istanbul là công cụ đo lường mức độ bao phủ mã nguồn (code coverage) phổ biến nhất dành cho JavaScript. `nyc` là giao diện dòng lệnh (CLI - Command Line Interface) chính thức của Istanbul, thường được sử dụng để bọc (wrap) các test runner nhằm thu thập và phân tích dữ liệu coverage.

### 2.2 Mục đích chính

Theo dõi, đo lường và báo cáo xem có bao nhiêu phần trăm mã nguồn đã thực sự được thực thi trong quá trình chạy các bài kiểm thử (Unit Test, Integration Test). Mục đích cuối cùng là giúp lập trình viên tìm ra những đoạn code chưa được test tới ("dead code" hoặc thiếu test case).

### 2.3 Ngôn ngữ/Nền tảng hỗ trợ

- **Ngôn ngữ:** JavaScript, TypeScript.
- **Nền tảng:** Node.js và môi trường Trình duyệt (Browser). Hoạt động tốt với hầu hết các framework/test runner như Mocha, AVA, Tape (Jest cũng sử dụng Istanbul ở bên dưới để đo coverage).

### 2.4 Cách công cụ hoạt động

Istanbul/nyc hoạt động dựa trên cơ chế **Instrumentation** (Nhúng mã):

1. Trước khi code được chạy, Istanbul đọc mã nguồn và phân tích thành Cây cú pháp trừu tượng (Abstract Syntax Tree - AST).
2. Chèn các biến đếm (counters) tàng hình vào các cấu trúc mã (hàm, câu lệnh, và các nhánh điều kiện if/else).
3. Khi test runner thực thi mã đã được nhúng này, các biến đếm sẽ tăng lên mỗi khi đoạn code tương ứng được chạy qua.
4. Sau khi test kết thúc, `nyc` thu thập giá trị của các biến đếm và xuất ra báo cáo.

### 2.5 Tính năng chính

- Đo lường 4 chỉ số bao phủ chính: **Statements** (Câu lệnh), **Branches** (Nhánh - if/else/switch), **Functions** (Hàm), và **Lines** (Dòng code).
- Hỗ trợ xuất báo cáo dưới nhiều định dạng: HTML trực quan (có highlight dòng code nào chưa chạy), LCOV, Cobertura, JSON, và bảng text trực tiếp trên terminal.
- Hỗ trợ Source-map: Theo dõi coverage chính xác về file code gốc (như TypeScript hoặc code ES6+ đã qua Babel) thay vì file code đã biên dịch ra JavaScript.
- Thiết lập ngưỡng (Thresholds): Cho phép cài đặt mức độ coverage tối thiểu (ví dụ: 80%). Nếu coverage thực tế thấp hơn, `nyc` sẽ trả về mã lỗi (exit code), giúp báo lỗi (fail) các pipeline CI/CD.

### 2.6 Trường hợp sử dụng phổ biến

- Tích hợp vào quy trình CI/CD pipelines (GitHub Actions, GitLab CI, Jenkins) để tự động bắt buộc kiểm tra code coverage đối với các Pull Request trước khi merge.
- Đánh giá chất lượng bộ test suite (Quality Gate) cho các dự án web backend bằng Node.js hoặc các thư viện npm.

### 2.7 Điểm mạnh

- Cài đặt và sử dụng cực kỳ đơn giản (thường chỉ cần thêm tiền tố `nyc` vào trước lệnh chạy test, ví dụ: `nyc mocha`).
- Giao diện báo cáo HTML sinh ra tự động rất chi tiết và dễ theo dõi.
- Cộng đồng người dùng lớn, là tiêu chuẩn công nghiệp (de-facto standard) cho JavaScript.
- Tương thích tốt với các công cụ build hiện đại thông qua hệ thống plugin (như `babel-plugin-istanbul`).

### 2.8 Giới hạn

- Quá trình instrumentation có thể làm tăng thời gian thực thi test suite, đặc biệt rõ ở các dự án có quy mô rất lớn.
- Việc cấu hình để hoạt động mượt mà với source-map đôi khi có thể phức tạp trong các dự án sử dụng cấu trúc Monorepo hoặc có quy trình build nhiều bước rườm rà.

### 2.9 Chi phí/Giấy phép

- Chi phí: Miễn phí hoàn toàn.
- Giấy phép: Mã nguồn mở phát hành dưới **ISC License**.

### 2.10 Hỗ trợ AI, nếu có

- Bản thân Istanbul/nyc là một công cụ phân tích tĩnh truyền thống, **không tích hợp AI trực tiếp**.
- Tuy nhiên, dữ liệu đầu ra của nó (định dạng JSON/LCOV) thường được dùng làm đầu vào cho các nền tảng đánh giá chất lượng mã nguồn có yếu tố AI (như SonarQube, Codecov) để từ đó AI gợi ý viết test tự động cho những phần mã chưa được phủ.

### 2.11 Tiềm năng demo

- **Rất cao và dễ hiểu cho seminar:** 1. Chuẩn bị một hàm tính toán đơn giản có nhánh `if/else`. 2. Viết một test case chỉ bao phủ trường hợp vào `if`. 3. Chạy lệnh `nyc` và hiển thị trên terminal bảng thống kê cho thấy chỉ số Branch coverage không đạt 100%. 4. Mở báo cáo HTML bằng trình duyệt để cho khán giả thấy trực quan dòng code chứa lệnh `else` bị bôi đỏ do chưa có test chạy qua.

### 2.12 Tài liệu tham khảo

- Website chính thức: [https://istanbul.js.org/](https://istanbul.js.org/)
- Kho lưu trữ GitHub `nyc`: [https://github.com/istanbuljs/nyc](https://github.com/istanbuljs/nyc)

---

## 3. JaCoCo

### 3.1 Tổng quan công cụ

JaCoCo (Java Code Coverage) là một thư viện mã nguồn mở tiêu chuẩn công nghiệp (de facto standard) giúp đo lường mức độ bao phủ mã nguồn cho hệ sinh thái Java. Nó được tạo ra bởi đội ngũ EclEmma (hiện thuộc Eclipse Foundation) và được sử dụng rộng rãi nhằm thay thế cho công cụ EclEmma cũ.

### 3.2 Mục đích chính

Đo lường tỉ lệ mã nguồn Java thực sự được thực thi trong quá trình chạy test (Unit Test, Integration Test). Báo cáo của JaCoCo giúp xác định các phần code chưa được kiểm thử (dead code), cải thiện chất lượng ứng dụng và đóng vai trò "chốt chặn" (coverage gate) để tự động đánh fail quá trình build nếu tỷ lệ coverage thấp hơn ngưỡng kỳ vọng.

### 3.3 Ngôn ngữ/Nền tảng hỗ trợ

- **Ngôn ngữ:** Java (hỗ trợ phân tích mã bytecode lên đến các phiên bản Java mới nhất như Java 21, 23).
- **Nền tảng:** Tích hợp sâu rộng với các công cụ build như Maven, Gradle, ANT; các IDE (thông qua EclEmma cho Eclipse) và các công cụ CI/CD, phân tích tĩnh như Jenkins, GitHub Actions, SonarQube, Codecov.

### 3.4 Cách công cụ hoạt động

Khác với Istanbul phân tích AST, JaCoCo hoạt động theo cơ chế **Instrumenting Bytecode (Nhúng mã vào bytecode) trong thời gian thực thi (on-the-fly)** thông qua một **Java Agent**:

1. Java Agent được gắn vào Java Virtual Machine (JVM) khi bắt đầu chạy test (thông qua execution goal `prepare-agent`).
2. Khi JVM tải các class, JaCoCo sẽ can thiệp và chèn tàng hình các biến đếm trực tiếp vào bytecode.
3. Khi mã chạy, các bộ đếm này lưu lại chính xác nhánh, dòng lệnh nào đã được gọi.
4. Thông tin thực thi được ghi vào file nhị phân (ví dụ: `jacoco.exec`). Test xong, execution goal `report` sẽ đọc file này và xuất ra báo cáo (HTML, XML). JaCoCo cũng cung cấp _offline instrumentation_ cho các môi trường đặc thù không hỗ trợ gắn Java Agent.

### 3.5 Tính năng chính

- Đo lường chi tiết nhiều cấp độ: **Instructions** (chỉ thị bytecode cấp thấp), **Branches** (quyết định if/switch), **Lines** (dòng mã), **Cyclomatic Complexity** (độ phức tạp), **Methods** và **Classes**.
- Báo cáo trực quan bằng mã màu sinh động: Xanh lá (đã bao phủ hết), Vàng (chỉ bao phủ một phần nhánh), Đỏ (chưa chạy qua). Ở các nhánh (branches), nó dùng biểu tượng hình thoi (diamonds) tương ứng.
- **Coverage Gate (`check` goal):** Thiết lập quy tắc giới hạn nghiêm ngặt (VD: tối thiểu 80% Line coverage, 70% Branch coverage).
- Gộp báo cáo (Multi-module aggregation) cho các dự án đa module.
- Lọc cấu hình (Exclusion) để bỏ qua các đoạn code do framework sinh ra tự động (như DTOs, code từ Lombok) nhằm giúp điểm coverage chính xác hơn.

### 3.6 Trường hợp sử dụng phổ biến

- Đóng vai trò là chốt kiểm duyệt (Quality Gate) trên CI/CD pipelines (Jenkins, GitHub Actions). Ví dụ cấu hình lệnh `mvn verify` tự động fail nếu PR mới làm giảm mức branch coverage.
- Xuất file `.xml` tổng hợp để upload lên các hệ thống quản lý như SonarQube hoặc Codecov.
- Kiểm tra chéo song song cùng công cụ Mutation Testing (như PIT) để đánh giá chất lượng các bài test trong dự án Java lớn.

### 3.7 Điểm mạnh

- Không cần sửa đổi hoặc tác động vào mã nguồn gốc (thao tác trực tiếp dưới mức bytecode).
- Tích hợp chuẩn hóa hoàn hảo với Maven/Gradle, thiết lập nhanh chóng chỉ với vài dòng XML.
- Nhẹ, rất nhanh (overhead cực thấp) và không phá vỡ cấu trúc project. Cộng đồng hỗ trợ lớn và luôn cập nhật song hành cùng các JDK mới nhất.

### 3.8 Giới hạn

- Vì đo ở cấp độ bytecode (C0 instructions) nên đôi lúc kết quả số lượng câu lệnh (instructions) hiển thị trên report sẽ khác biệt so với số lượng dòng mã (lines of code) của source gốc.
- Đối với các framework tự động chỉnh sửa bytecode khác hoặc một vài ClassLoader đặc biệt, quá trình on-the-fly agent có thể bị xung đột, buộc phải dùng giải pháp Offline Instrumentation phức tạp hơn.
- Coverage cao tạo ra "ảo giác an toàn": JaCoCo chỉ khẳng định code "đã được gọi qua", chứ không xác minh xem test đó có chứa các hàm `assert` chuẩn xác hay không.

### 3.9 Chi phí/Giấy phép

- Chi phí: Hoàn toàn miễn phí.
- Giấy phép: Mã nguồn mở theo giấy phép Eclipse Public License (EPL).

### 3.10 Hỗ trợ AI, nếu có

- JaCoCo cốt lõi là công cụ truyền thống. Tuy nhiên, định dạng đầu ra chuẩn mực (XML) của nó là cơ sở dữ liệu quan trọng đầu vào cho các công cụ AI Testing Agent (như KaneAI của TestMu, hoặc QA agents) để các agent này tự động phân tích vùng "màu đỏ" và sinh test case bổ sung hoặc tối ưu bug fixes bằng GenAI.

### 3.11 Tiềm năng demo

- **Cao:** Demo tạo một dự án Maven (đặt cấu hình `pom.xml` với `jacoco-maven-plugin`).
  1. Chạy test `mvn test` và mở file HTML để show các "hình thoi (diamond) màu vàng" chứng minh code bị rẽ nhánh chưa test.
  2. Bật cấu hình `jacoco:check` (ví dụ quy định tỉ lệ 80%), chạy lệnh `mvn verify` và chỉ ra log build thất bại (`BUILD FAILURE`) để demo tính năng Coverage Gate.

### 3.12 Tài liệu tham khảo

- EclEmma - JaCoCo Homepage: https://www.jacoco.org/jacoco/
- JaCoCo Code Coverage in Java 2026 Guide: https://qaskills.sh/blog/jacoco-code-coverage-java-guide-2026
- Reporting code coverage using Maven and JaCoCo plugin: https://www.testmuai.com/blog/reporting-code-coverage-using-maven-and-jacoco-plugin/

---

## 4. Ghi chú tổng kết

Cả **Istanbul/nyc (JS)** và **JaCoCo (Java)** đều là những công cụ nền tảng trong việc đánh giá chất lượng test, tuy nhiên chúng chỉ đo lường một khía cạnh cơ bản khi so sánh với các kỹ thuật nâng cao hơn như Mutation Testing.

- **Code Coverage (Istanbul/nyc, JaCoCo):** Cho biết bộ test đã chạy qua những phần nào của mã nguồn. Công cụ này trả lời cho câu hỏi: _"Code đã được test chạm tới chưa?"_.
- **Mutation Testing (như StrykerJS cho JS hoặc PIT cho Java):** Cho biết bộ test có thực sự phát hiện được lỗi logic khi mã nguồn bị thay đổi hay không. Kỹ thuật này trả lời cho câu hỏi: _"Test case có bắt được lỗi không?"_.

Vì vậy, Istanbul/JaCoCo phù hợp để làm bức tường phòng ngự vòng ngoài (kiểm tra mức độ bao phủ cơ bản), còn các công cụ Mutation Testing phù hợp để đánh giá sâu hơn về _test effectiveness_ (hiệu quả kiểm thử).

Trong buổi seminar, hai nhóm công cụ này có thể kết hợp với nhau tạo thành một kịch bản thuyết trình và demo hoàn hảo:

1. Dùng Istanbul/nyc hoặc JaCoCo để cho thấy một bộ test có thể dễ dàng đạt Coverage rất cao (thậm chí 100%).
2. Dùng StrykerJS hoặc PIT tạo ra các "đột biến" (mutation) trên code để cho thấy: Dù coverage cao, bộ test vẫn có thể rất yếu (không phát hiện được lỗi do thiếu hàm assert).
3. Bổ sung các test case với logic chặt chẽ và tốt hơn.
4. Chạy lại công cụ Mutation Testing để chứng minh chất lượng (effectiveness) của test suite đã thực sự được cải thiện.
