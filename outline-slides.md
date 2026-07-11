# DÀN Ý BÀI THUYẾT TRÌNH: MUTATION TESTING - KIỂM THỬ CỦA KIỂM THỬ

- **Tổng thời lượng:** ~25-30 phút.

---

### Slide 1: Tiêu đề & Giới thiệu (1 phút)

- **Tiêu đề:** Mutation Testing: Đánh giá chất lượng bộ kiểm thử vượt ra ngoài Code Coverage.
- **Nội dung chính:**
  - Thách thức của việc đảm bảo chất lượng phần mềm hiện đại.
  - Câu hỏi cốt lõi: "Ai kiểm tra các bài kiểm tra của bạn?" (Who tests the tests?).
  - Giới thiệu Mutation Testing như một "người gác cổng" cho Test Effectiveness.
- **Speaker Notes:** Chào mừng mọi người. Hôm nay chúng ta sẽ tìm hiểu vì sao Code Coverage 100% vẫn có thể để lọt lỗi nghiêm trọng và cách Mutation Testing giúp chúng ta xây dựng bộ test thực sự tin cậy.
- **Đồ họa gợi ý:** Hình ảnh một người soi kính lúp vào các đoạn mã test hoặc logo các công cụ lớn (Stryker, PIT).

---

### Slide 2: Ảo tưởng về Code Coverage (2 phút)

- **Tiêu đề:** Tại sao Code Coverage là chưa đủ?
- **Nội dung chính:**
  - Code Coverage đo lường **định lượng**: Những dòng code nào đã chạy qua?.
  - Vấn đề "ảo tưởng an toàn": Coverage cao nhưng vẫn thiếu Assertion (khẳng định).
  - Chỉ số này không phát hiện được lỗi logic hoặc các trường hợp biên (boundary cases).
  - Lập trình viên đôi khi viết test chỉ để "đối phó" với CI pipeline.
- **Speaker Notes:** Coverage chỉ là ranh giới dưới (Lower Bound). Nó cho biết code đã chạy, nhưng không đảm bảo test có khả năng bắt lỗi.
- **Đồ họa gợi ý:** Biểu đồ tảng băng trôi: Phần nổi là Coverage (Quantity), phần chìm là Test Effectiveness (Quality).

---

### Slide 3: Mutation Testing là gì? (2 phút)

- **Tiêu đề:** Khái niệm Mutation Testing
- **Nội dung chính:**
  - Kỹ thuật tự động thay đổi nhỏ cú pháp mã nguồn (tạo ra các **Mutants**).
  - Nếu bộ test thất bại (Fail) -> Mutant bị **Killed** (Tốt).
  - Nếu bộ test vẫn vượt qua (Pass) -> Mutant **Survived** (Test yếu).
  - Mục tiêu: Đánh giá độ nhạy bén của bộ test trước các thay đổi sai lệch.
- **Speaker Notes:** Thay vì tìm bug trong code, chúng ta cố tình đưa "vi khuẩn" (mutants) vào code để xem "hệ miễn dịch" (bộ test) có tiêu diệt được chúng hay không.
- **Đồ họa gợi ý:** Sơ đồ minh họa: Original Code -> Mutant -> Test Suite -> Killed/Survived.

---

### Slide 4: Quy trình thực hiện (Workflow) (2 phút)

- **Tiêu đề:** Quy trình Mutation Testing tiêu chuẩn
- **Nội dung chính:**
  1.  Chạy bộ test trên code gốc (phải Pass hết).
  2.  Tạo các Mutants bằng các toán tử đột biến (Mutation Operators).
  3.  Chạy lại bộ test trên từng Mutant.
  4.  Phân loại kết quả (Killed, Survived, Timeout, No Coverage).
  5.  Phân tích báo cáo và cải thiện bộ test.
- **Speaker Notes:** Các công cụ hiện đại như PIT hay Stryker tối ưu bước này bằng cách chỉ chạy những bài test có đi qua vùng code bị đột biến.
- **Đồ họa gợi ý:** Sơ đồ vòng lặp workflow từ bước chọn code đến bước tính Mutation Score.

---

### Slide 5: Các toán tử đột biến (Mutation Operators) (2 phút)

- **Tiêu đề:** Mutation Operators - Cách tạo ra "biến dị"
- **Nội dung chính:**
  - **Toán tử số học:** Đổi `+` thành `-`, `*` thành `/`.
  - **Toán tử quan hệ:** Đổi `>=` thành `>`, `==` thành `!=`.
  - **Logic & Boolean:** Đổi `&&` thành `||`, `true` thành `false`.
  - **Thay đổi giá trị trả về:** Đổi `return object` thành `return null`.
  - **Xóa câu lệnh:** Loại bỏ các lời gọi hàm (Side-effects).
- **Speaker Notes:** Mỗi toán tử mô phỏng một lỗi lập trình thực tế mà con người thường mắc phải, đặc biệt là lỗi tại các điểm biên.
- **Đồ họa gợi ý:** Bảng so sánh "Original Code" vs "Mutant Code" cho 3-4 loại toán tử phổ biến.

---

### Slide 6: Ví dụ mã nguồn: Killed vs Survived (Demo) (3 phút)

- **Tiêu đề:** Minh họa thực tế: Sức mạnh của Mutation
- **Mã nguồn ví dụ (JavaScript/Jest):**

```javascript
// Mã nguồn gốc: Kiểm tra tuổi bầu cử
const canVote = (age) => age >= 18;

// Bộ Test 1: Coverage 100% nhưng yếu
test("can vote", () => {
  expect(canVote(20)).toBe(true);
});

// Mutation: Đổi >= thành >
// canVote_Mutant = (age) => age > 18;
// Test trên vẫn PASS -> Mutant SURVIVED! (Thiếu boundary test tại 18)
```

- **Speaker Notes:** Ở đây, test case `age=20` vẫn đúng cho cả code gốc và code lỗi. Mutation Testing vạch trần việc chúng ta quên kiểm tra giá trị biên `18`.
- **Đồ họa gợi ý:** Highlight dòng code bị thay đổi và trạng thái "Survived" màu đỏ trên report.

---

### Slide 7: Chỉ số Mutation Score (2 phút)

- **Tiêu đề:** Mutation Score - Thước đo chất lượng thực sự
- **Nội dung chính:**
  - **Công thức thực tế:** $\frac{Killed + Timeout}{Total Mutants} \times 100\%$.
  - **Ý nghĩa các trạng thái:**
    - **Killed:** Test phát hiện được lỗi.
    - **Survived:** Test lỏng lẻo hoặc thiếu assertion.
    - **No Coverage:** Code hoàn toàn chưa được test.
    - **Timeout:** Mutant gây vòng lặp vô hạn (thường tính là Killed).
- **Speaker Notes:** Mục tiêu là đưa Mutation Score càng gần 100% càng tốt. Một bộ test mạnh phải tiêu diệt được hầu hết các đột biến.
- **Đồ họa gợi ý:** Hình ảnh một dashboard báo cáo với biểu đồ tròn thể hiện tỷ lệ các trạng thái.

---

### Slide 8: So sánh: Coverage vs Mutation (2 phút)

- **Tiêu đề:** Code Coverage vs Mutation Testing
- **Nội dung chính:**
  | Tiêu chí | Code Coverage | Mutation Testing |
  | :--- | :--- | :--- |
  | **Mục tiêu** | Tìm mã nguồn chưa chạy qua | Đánh giá chất lượng bộ test |
  | **Bản chất** | Định lượng (Quantity) | Định tính (Effectiveness) |
  | **Chi phí** | Rất nhanh, rẻ | Chậm, tốn tài nguyên CPU/RAM |
  | **Điểm yếu** | Dễ bị lừa bởi test thiếu assertion | Vấn đề Equivalent Mutants |
- **Speaker Notes:** Đừng coi chúng là đối thủ. Hãy dùng Coverage để tìm vùng code bị bỏ quên, và dùng Mutation để đảm bảo các vùng quan trọng được test chặt chẽ.
- **Đồ họa gợi ý:** Bảng so sánh đối chiếu rõ ràng.

---

### Slide 9: Equivalent Mutants & Giới hạn (2 phút)

- **Tiêu đề:** Những thách thức và giới hạn
- **Nội dung chính:**
  - **Equivalent Mutants:** Thay đổi cú pháp nhưng hành vi không đổi (Ví dụ: `i++` thành `++i` trong vòng lặp đơn) -> Không bao giờ bị giết.
  - **Chi phí thực thi:** Chạy test hàng nghìn lần cho hàng nghìn mutants có thể làm chậm CI/CD.
  - **Sự bùng nổ tổ hợp:** Số lượng mutant tăng vọt theo quy mô dự án.
  - **Giải pháp:** Chỉ chạy trên code thay đổi (Incremental) hoặc vùng business logic cốt lõi.
- **Speaker Notes:** Việc xác định Equivalent Mutant là bài toán không thể tự động hóa hoàn toàn, đôi khi cần con người review thủ công.
- **Đồ họa gợi ý:** Ví dụ mã nguồn về tính chất giao hoán `a + b` sang `b + a` để minh họa Equivalent Mutant.

---

### Slide 10: Tối ưu Test Effectiveness (2 phút)

- **Tiêu đề:** Nâng cao hiệu quả kiểm thử
- **Nội dung chính:**
  - **Hard vs Soft Assertions:** Dùng Hard Assert cho điều kiện tiên quyết, Soft Assert cho kiểm tra form/nhiều thuộc tính.
  - **Phát hiện lỗi sớm:** Assertion đúng chỗ giảm 33% công sức debug.
  - **Kiểm tra Side-effects:** Không chỉ check giá trị trả về, hãy check DB, Email, Logs.
  - **Risk-based Testing:** Ưu tiên Mutation Testing cho module tài chính, bảo mật.
- **Speaker Notes:** Mutation Testing giúp biến các bài test thành "tài liệu sống" mô tả chính xác các quy tắc nghiệp vụ.
- **Đồ họa gợi ý:** Hình ảnh minh họa các checkpoint (assertions) trong một luồng xử lý dữ liệu.

---

### Slide 11: Toàn cảnh công cụ (2 phút)

- **Tiêu đề:** Hệ sinh thái công cụ Mutation Testing
- **Nội dung chính:**
  - **Java:** PIT (Phổ biến nhất, nhanh nhờ bytecode mutation).
  - **JS/TS:** StrykerJS (Mạnh mẽ, báo cáo HTML đẹp).
  - **Python:** Mutmut (Dễ dùng, nhanh), Cosmic Ray (Phân tán).
  - **C#/.NET:** Stryker.NET.
  - **PHP:** Infection (Dựa trên AST).
- **Speaker Notes:** Mỗi ngôn ngữ đều có công cụ đặc thù. Điểm chung là chúng đang ngày càng tối ưu để tích hợp tốt hơn vào CI pipeline.
- **Đồ họa gợi ý:** Ma trận logo các công cụ chia theo ngôn ngữ lập trình.

---

### Slide 12: Bảng so sánh các công cụ (Đặc biệt)

- **Tiêu đề:** So sánh chi tiết các công cụ phổ biến

| Công cụ         | Ngôn ngữ | Mutation Type  | CI Integration            | Hiệu năng                 | License     |
| :-------------- | :------- | :------------- | :------------------------ | :------------------------ | :---------- |
| **PIT**         | Java/JVM | Bytecode       | Rất tốt (Maven/Gradle)    | Cao (Fast)                | Open Source |
| **StrykerJS**   | JS/TS    | Source code    | Tốt (GitHub Actions, v.v) | Trung bình                | Apache 2.0  |
| **Mutmut**      | Python   | AST            | Khá                       | Cao (Cache)               | BSD-3       |
| **Infection**   | PHP      | AST            | Tốt                       | Trung bình                | BSD-3       |
| **Major**       | Java     | AST            | Trung bình                | Cao (Compiler-integrated) | Miễn phí    |
| **Cosmic Ray**  | Python   | AST            | Khá                       | Thấp (Phân tán)           | BSD-2       |
| **Stryker.NET** | C#       | Source code    | Tốt (dotnet CLI)          | Trung bình                | Open Source |
| **JaCoCo/nyc**  | Java/JS  | _Chỉ Coverage_ | Rất tốt                   | Rất cao                   | EPL/ISC     |

- _Ghi chú:_ JaCoCo và Istanbul (nyc) không phải mutation tool nhưng thường dùng làm baseline.

---

### Slide 13: Khuyến nghị & Chiến lược (2 phút)

- **Tiêu đề:** Lựa chọn công cụ & Chiến lược triển khai
- **Nội dung chính:**
  1.  **Dự án Java lớn:** Ưu tiên **PIT** vì tính trưởng thành và hiệu năng vượt trội nhờ Bytecode mutation.
  2.  **JS Front-end (React/Angular):** Sử dụng **StrykerJS** nhờ hỗ trợ tuyệt vời cho nhiều test runner (Jest, Mocha) và report trực quan.
  3.  **Dự án Python nhỏ/vừa:** **Mutmut** là lựa chọn số 1 vì cài đặt cực nhanh và có cơ chế cache thông minh.
  4.  **CI Pipeline:** Chỉ nên chạy Mutation Testing trên các tệp thay đổi (**Incremental**) để đảm bảo tốc độ feedback.
- **Speaker Notes:** Đừng cố đạt 100% Mutation Score ngay lập tức. Hãy bắt đầu với những module quan trọng nhất.
- **Đồ họa gợi ý:** Cây quyết định (Decision Tree) giúp chọn tool dựa trên ngôn ngữ và quy mô dự án.

---

### Slide 14: Kết luận & Hỏi đáp (2 phút)

- **Tiêu đề:** Kết luận: Hãy để Mutation Testing bảo vệ bạn
- **Nội dung chính:**
  - Mutation Testing là thước đo chất lượng test tốt nhất hiện nay.
  - Giúp loại bỏ sự tự mãn khi thấy Coverage cao.
  - Đầu tư vào Mutation Testing là đầu tư vào sự ổn định lâu dài của hệ thống.
  - "Đừng chỉ chạy code, hãy kiểm chứng logic".
- **Speaker Notes:** Cảm ơn các bạn đã lắng nghe. Mutation Testing có thể tốn thời gian lúc đầu, nhưng nó sẽ cứu bạn khỏi những bug logic "ngớ ngẩn" trong tương lai. Mọi người có câu hỏi nào không?
- **Đồ họa gợi ý:** Hình ảnh một tấm khiên bảo vệ mã nguồn.

---

**Tổng thời lượng dự kiến:** ~26 phút.
