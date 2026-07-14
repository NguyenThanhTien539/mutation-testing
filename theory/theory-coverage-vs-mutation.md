# Code Coverage và Mutation Testing

## 1. Mục tiêu

Nghiên cứu các yếu tố cốt lõi phân định giữa số lượng và chất lượng của một bộ kiểm thử (Test Suite) thông qua hai phương pháp đánh giá: Code Coverage và Mutation Testing. Mục tiêu của phần này là hiểu rõ ranh giới giữa việc "thực thi mã nguồn" và "xác minh tính đúng đắn của mã nguồn", nhận diện các rủi ro bảo mật và lỗi logic tiềm ẩn khi chỉ phụ thuộc vào chỉ số bao phủ (Coverage), đồng thời tận dụng Mutation Testing để đánh giá mức độ hiệu quả (Test Effectiveness) và độ chặt chẽ của các kịch bản kiểm thử, từ đó xây dựng các hệ thống phần mềm có độ tin cậy cao.

## 2. Câu hỏi chính

- **Code Coverage đo lường điều gì?**
- **Mutation Testing đo lường điều gì?**
- **Vì sao coverage có thể cao nhưng test vẫn yếu?**
- **Vì sao Mutation Testing hữu ích khi đánh giá Test Effectiveness?**

Trả lời ngắn gọn:

Code Coverage đo lường tỷ lệ mã nguồn được thực thi khi chạy test (statement/branch/path), trong khi Mutation Testing đo lường khả năng test phát hiện được lỗi logic thông qua việc chèn các mutant vào code rồi kiểm tra test có fail hay không. Coverage có thể cao nhưng test vẫn yếu nếu thiếu assertion; Mutation Testing hữu ích vì nó buộc lộ ra chính xác những chỗ test "chạy qua nhưng không xác minh" đó.

## 3. Ghi chú chính

### 3.1 Nguyên lý của Code Coverage (Độ bao phủ mã nguồn)

- **Giá trị cốt lõi**: Là một công cụ tuyệt vời để phát hiện những vùng mã nguồn _chưa từng được kiểm thử_ (Dead code hoặc Missing tests).
- **Các cấp độ đo lường (Metrics)**:
  - _Statement Coverage_: Đo tỷ lệ các câu lệnh đã chạy.
  - _Branch Coverage_: Đo tỷ lệ các nhánh điều kiện (if/else, switch) đã được đánh giá cả True và False.
  - _Path Coverage_: Đo lường tất cả các luồng thực thi có thể có (thường rất khó đạt 100% trong hệ thống phức tạp).
- **Ảo tưởng về sự an toàn**: Việc đặt mục tiêu ép buộc 100% Code Coverage thường dẫn đến "Anti-pattern" - lập trình viên viết test chỉ để chạy qua code nhằm đối phó với CI/CD pipeline, bỏ qua việc kiểm chứng logic nghiệp vụ.

### 3.2 Khái niệm về Mutation Testing (Kiểm thử đột biến)

Mutation testing là kỹ thuật tự động thay đổi cú pháp mã nguồn gốc (tạo ra các biến dị - mutants) và chạy lại bộ test để xem test có thất bại (fail) hay không.

- **Bản chất**: Nếu test fail, mutant bị "tiêu diệt" (Killed) -> Test tốt. Nếu test vẫn pass, mutant "sống sót" (Survived) -> Test yếu.
- **Các toán tử đột biến (Mutation Operators) phổ biến**:
  - Thay đổi toán tử toán học: `+` thành `-`, `*` thành `/`.
  - Thay đổi toán tử quan hệ: `>` thành `>=`, `==` thành `!=`.
  - Sửa đổi giá trị trả về: Đổi chuỗi, đổi `true` thành `false`.
- **Phân biệt với Chaos Engineering**: Trong khi Chaos Engineering tạo ra sự cố ở cấp độ hạ tầng mạng/hệ thống, Mutation Testing tạo ra sự cố ở cấp độ cú pháp mã nguồn tại thời điểm build/test.

### 3.3 Phân tích so sánh chi tiết

| Tiêu chí              | Code Coverage                           | Mutation Testing                                          |
| --------------------- | --------------------------------------- | --------------------------------------------------------- |
| **Mục đích chính**    | Tìm mã nguồn chưa được test             | Đánh giá chất lượng của bộ test                           |
| **Bản chất đo lường** | Định lượng (Quantity)                   | Định tính (Quality / Effectiveness)                       |
| **Chi phí thực thi**  | Rất nhanh, chi phí tính toán thấp       | Rất chậm, tiêu tốn cực lớn tài nguyên                     |
| **Kết quả kỳ vọng**   | % mã được bao phủ                       | % biến dị bị tiêu diệt (Mutation Score)                   |
| **Điểm yếu**          | Dễ bị đánh lừa bởi test thiếu assertion | Thời gian chạy lâu, có thể tạo ra các mutants tương đương |

## 4. Ví dụ

### 4.1 Các yếu tố thực tế ảnh hưởng đến Test Effectiveness

- **Thiếu xác thực kết quả (Missing Assertions)**: Lỗi phổ biến nhất khi theo đuổi Coverage. Hàm được gọi, không sinh ra lỗi (Exception), test Pass, nhưng dữ liệu trả về hoàn toàn sai.
- **Kiểm tra lỏng lẻo (Weak Assertions)**: Chỉ kiểm tra mã trạng thái trả về (ví dụ: HTTP 200) mà không kiểm tra cấu trúc dữ liệu thực tế bên trong.

### 4.2 Code mẫu minh họa

Dưới đây là ví dụ minh họa bằng Node.js. Chú ý cấu trúc thiết kế ở đây tuân thủ nguyên tắc gom logic xử lý request/response trực tiếp vào file `routes` mà không sử dụng thư mục `controller` riêng biệt.

**Mã nguồn API (routes/booking.js) - Quản lý đặt phòng Homestay:**

```javascript
const express = require("express");
const router = express.Router();

router.post("/booking", (req, res) => {
  const { roomType, days } = req.body;

  if (days <= 0) {
    return res.status(400).json({ error: "Số ngày thuê không hợp lệ" });
  }

  // Logic tính giá: Phòng VIP giá 1000, phòng thường giá 500
  let totalPrice = roomType === "VIP" ? 1000 * days : 500 * days;

  return res.status(200).json({ status: "success", total: totalPrice });
});

module.exports = router;
```

**Bộ Test 100% Coverage nhưng vô dụng (booking.test.js):**

```javascript
const request = require("supertest");
const app = require("../app"); // Ứng dụng Express đã mount router

describe("Homestay Booking Route - Coverage Test", () => {
  it("Thực thi nhánh đặt phòng VIP", async () => {
    // Gọi API với phòng VIP (Đạt coverage nhánh True của toán tử ba ngôi)
    await request(app).post("/booking").send({ roomType: "VIP", days: 2 });
    // LỖI NGHIÊM TRỌNG: Không có lệnh `expect()` nào kiểm tra kết quả!
  });

  it("Thực thi nhánh đặt phòng Thường", async () => {
    // Gọi API với phòng Normal (Đạt coverage nhánh False)
    await request(app).post("/booking").send({ roomType: "Normal", days: 3 });
  });

  it("Thực thi nhánh lỗi ngày <= 0", async () => {
    // Đạt coverage nhánh If
    await request(app).post("/booking").send({ roomType: "VIP", days: -1 });
  });
});
```

### 4.3 Phân tích một ca kiểm thử vô dụng (100% Coverage nhưng không có Assertion)

Giả sử chúng ta có một hệ thống tính tiền đặt phòng Homestay. Logic hệ thống rất đơn giản: lấy "số ngày thuê" nhân với "giá phòng".

Một lập trình viên viết một bộ kiểm thử gọi hàm tính tiền này với đầy đủ các trường hợp: phòng VIP, phòng thường, số ngày âm.

- **Kết quả Code Coverage:** Đạt 100% vì tất cả các nhánh điều kiện (if/else) trong hàm đều đã được thực thi.
- **Vấn đề:** Trong bộ kiểm thử đó, lập trình viên quên không viết bất kỳ câu lệnh `assert` hoặc `expect` nào để so sánh số tiền trả về với kết quả đúng (ví dụ: mong đợi 3 ngày VIP là 3000k).

**Khi áp dụng Mutation Testing:** Hệ thống Mutation Testing tự động can thiệp vào mã nguồn và đổi dấu nhân `*` thành dấu cộng `+` (Tiền = Số ngày + Giá phòng). Lúc này, vì bộ test hoàn toàn không kiểm tra kết quả đầu ra (thiếu assertion), nó vẫn chạy mượt mà và báo PASS. Biến dị đã "sống sót" (Mutant Survived), qua đó vạch trần lỗ hổng nghiêm trọng của bộ test: Độ bao phủ 100% nhưng không hề có khả năng bắt lỗi logic.

## 5. Công cụ hỗ trợ lý thuyết này

Đây là chủ đề mà việc khảo sát tool của nhóm ánh xạ trực tiếp và rõ ràng nhất: 11 công cụ đã khảo sát chia thành đúng hai nhóm của lý thuyết này.

| Nhóm                               | Công cụ                                                                                                    | Đo lường gì                                    | Vai trò theo lý thuyết mục 5                                                                            |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **Code Coverage (Lower Bound)**    | Istanbul/nyc (JS/TS), JaCoCo (Java), Jest Coverage (JS/TS), Coverage.py (Python)                           | % statement/branch/function/line được chạy qua | Tìm code chưa được test, không xác minh assertion — đúng vai trò "ranh giới dưới".                      |
| **Mutation Testing (Upper Bound)** | StrykerJS, Stryker.NET (JS/TS, C#), PIT (Java), Mutmut, Cosmic Ray (Python), Infection (PHP), Major (Java) | % mutant bị killed (Mutation Score)            | Xác minh assertion có đủ mạnh để bắt lỗi logic không — đúng vai trò "ranh giới trên", "người gác cổng". |

**Bằng chứng thực nghiệm của nhóm** (`demo/strykerjs-setup/setup-steps.md`) tái hiện chính xác kịch bản ở mục 4.3 nhưng bằng số liệu thật thay vì ví dụ giả định: bộ test ban đầu cho `Register.jsx` có coverage nhưng chỉ 1 assertion, khiến 27/35 mutant có coverage vẫn `survived` — tức Mutation Score phần covered chỉ 22.86%, trong khi nếu chỉ đo bằng coverage thông thường (Jest Coverage/Istanbul), các dòng code đó vẫn hiển thị "đã covered" và không lộ ra vấn đề gì. Đây là minh chứng trực tiếp cho luận điểm cốt lõi: coverage cao không đảm bảo test có khả năng phát hiện lỗi logic.

Bốn công cụ đo coverage (Istanbul/nyc, JaCoCo, Jest Coverage, Coverage.py) không có khái niệm "mutant" hay "killed/survived" trong report của chúng — đây chính là ranh giới kỹ thuật cụ thể hoá cho phân biệt "Lower Bound" và "Upper Bound" nêu ở mục 5 bên dưới. Đáng chú ý, Coverage.py còn cho thấy hai nhóm này không hoàn toàn tách biệt: Mutmut (nhóm Upper Bound) trực tiếp đọc dữ liệu do Coverage.py sinh ra để tối ưu phạm vi mutate (`tool-survey-coveragepy.md`), tức một coverage tool có thể làm nền tảng cho một mutation tool.

## 6. Ý chính cần ghi nhớ

- **Code Coverage là ranh giới dưới (Lower Bound)**: Nó cho biết mức tối thiểu bạn cần làm để bao phủ hệ thống, không phải là thước đo tuyệt đối về sự an toàn. Hãy dùng nó để tìm những đoạn code bị bỏ quên.
- **Mutation Testing là ranh giới trên (Upper Bound)**: Là phép thử khắc nghiệt nhất cho Test Effectiveness. Nó đóng vai trò như "người gác cổng" kiểm tra chính các bài kiểm tra của bạn.
- **Quy trình kết hợp tối ưu**:
  1. Viết test để thiết kế hệ thống và bao phủ các luồng nghiệp vụ (đảm bảo Coverage ở mức hợp lý, khoảng 80-85%).
  2. Sử dụng Hard/Soft Assertions chặt chẽ để verify từng thuộc tính dữ liệu và side-effects.
  3. Áp dụng Mutation Testing vào các module cốt lõi (như module tính toán tài chính, phân quyền bảo mật) để đảm bảo không một sai sót logic nào có thể lọt qua.
- **Đánh đổi tài nguyên**: Không nên chạy Mutation Testing trên toàn bộ dự án vì thời gian build sẽ rất lâu. Hãy áp dụng chiến lược Risk-based testing (kiểm thử dựa trên rủi ro) để chỉ chạy Mutation ở các vùng mã nhạy cảm.
- 11 công cụ đã khảo sát của nhóm chia đúng thành 2 nhóm của lý thuyết này: 4 coverage tool và 7 mutation tool.

## 7. Tài liệu tham khảo

- [Martin Fowler - Mutation Testing](https://martinfowler.com/bliki/MutationTesting.html)
- [Google Testing Blog - Code Coverage Best Practices](https://testing.googleblog.com/2020/08/code-coverage-best-practices.html)
- [IEEE Xplore - An Analysis and Survey of the Development of Mutation Testing](https://ieeexplore.ieee.org/document/629606)
