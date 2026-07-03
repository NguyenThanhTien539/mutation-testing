# Mutation Score và các thuật ngữ trong báo cáo

## 1. Mục tiêu
Nghiên cứu về Mutation Score, công thức tính toán và ý nghĩa của các thuật ngữ phổ biến trong báo cáo kiểm thử đột biến (Mutation Report).

## 2. Câu hỏi chính

### Mutation Score là gì?
**Mutation Score (Điểm đột biến)** là một chỉ số (thường tính bằng phần trăm) đo lường mức độ hiệu quả của một bộ kiểm thử (test suite) trong việc phát hiện các lỗi (đột biến) được đưa vào mã nguồn một cách cố ý. Điểm đột biến càng cao chứng tỏ bộ kiểm thử càng mạnh mẽ và có khả năng phát hiện lỗi tốt.

### Mutation Score được tính như thế nào?
#### Công thức lý thuyết (Theoretical Formula):
Trong lý thuyết, các mutant tương đương (Equivalent Mutants) không thể bị tiêu diệt bằng bất kỳ bộ test nào, do đó chúng phải được loại bỏ khỏi tổng số mutant trước khi tính toán:
$$\text{Mutation Score} = \left( \frac{\text{Killed Mutants}}{\text{Total Mutants} - \text{Equivalent Mutants}} \right) \times 100\%$$
*Trong đó, Killed Mutants thường bao gồm cả các mutant bị Timeout.*

#### Công thức thực tế (Practical Formula - dùng trong các công cụ như Pitest, Stryker):
Vì việc tự động nhận diện Equivalent Mutants là một bài toán không thể tự động hóa hoàn toàn (undecidable problem), các công cụ thực tế thường tính theo công thức:
$$\text{Mutation Score} = \left( \frac{\text{Killed Mutants} + \text{Timeout Mutants}}{\text{Total Mutants}} \right) \times 100\%$$
Hoặc phân chia chi tiết theo Stryker:
$$\text{Mutation Score} = \left( \frac{\text{Killed} + \text{Timeout}}{\text{Killed} + \text{Timeout} + \text{Survived} + \text{No Coverage}} \right) \times 100\%$$

### Các thuật ngữ killed, survived, timeout, no coverage và equivalent mutant có nghĩa là gì?
- **Killed (Đã tiêu diệt)**: Mutant bị tiêu diệt khi có ít nhất một ca kiểm thử (test case) bị thất bại (fail) do sự thay đổi của đột biến. Điều này chứng tỏ bộ kiểm thử đã phát hiện ra lỗi đột biến này thành công.
- **Survived (Sống sót)**: Mutant sống sót khi toàn bộ các ca kiểm thử đều vượt qua (pass) mặc dù mã nguồn đã bị thay đổi bởi đột biến. Điều này phản ánh bộ kiểm thử chưa đủ bao phủ hoặc thiếu các câu lệnh khẳng định (assertions) để phát hiện sự thay đổi logic này.
- **Timeout (Quá thời gian)**: Mutant làm cho chương trình rơi vào vòng lặp vô hạn hoặc chạy quá thời gian quy định (thường do đột biến thay đổi điều kiện dừng của vòng lặp hoặc đệ quy). Thông thường, trạng thái này được tính là **Killed** vì hệ thống kiểm thử phát hiện ra sự bất thường.
- **No Coverage (Không có độ bao phủ)**: Mutant được tạo ra ở dòng mã nguồn không được bất kỳ ca kiểm thử nào thực thi qua. Do không được chạy qua, mutant này mặc định sống sót và cho thấy vùng mã nguồn đó hoàn toàn chưa được kiểm thử.
- **Equivalent Mutant (Mutant tương đương)**: Một mutant có cú pháp khác với mã gốc nhưng có ngữ nghĩa (hành vi) hoàn toàn trùng khớp với mã gốc. Vì hành vi không đổi, không một ca kiểm thử nào có thể tiêu diệt được mutant này.

---

## 3. Ghi chú chính
- Điểm đột biến (Mutation Score) phản ánh **chất lượng của bộ test**, khác với kiểm thử độ bao phủ dòng lệnh (Line/Branch Coverage) chỉ phản ánh **số lượng dòng code được chạy qua**. Một bộ test có coverage 100% vẫn có thể có Mutation Score thấp nếu thiếu các kiểm tra biên hoặc thiếu câu lệnh khẳng định (`assert`).
- Việc giảm thiểu **Equivalent Mutants** là một trong những thách thức lớn nhất trong kiểm thử đột biến.

---

## 4. Ví dụ
Giả sử chúng ta chạy kiểm thử đột biến trên một project và nhận được kết quả sau:
- Tổng số mutant sinh ra: 120
- Số mutant bị tiêu diệt (Killed): 80
- Số mutant bị quá giờ (Timeout): 5
- Số mutant sống sót (Survived): 20
- Số mutant không được bao phủ (No Coverage): 10
- Số mutant tương đương (Equivalent) được xác định bằng thủ công: 5

#### Tính toán theo Lý thuyết:
Loại trừ 5 equivalent mutants ra khỏi mẫu số:
$$\text{Mutation Score} = \left( \frac{80 + 5}{120 - 5} \right) \times 100\% = \left( \frac{85}{115} \right) \times 100\% \approx 73.91\%$$

#### Tính toán theo Thực tế (công cụ Stryker/Pitest):
$$\text{Mutation Score} = \left( \frac{80 + 5}{120} \right) \times 100\% = \left( \frac{85}{120} \right) \times 100\% \approx 70.83\%$$

---

## 5. Ý chính cần ghi nhớ
- **Mutation Score** là thước đo độ nhạy bén của bộ test suite trước những thay đổi logic lỗi.
- Mục tiêu tối thượng của kiểm thử đột biến là nâng cao Mutation Score càng gần 100% càng tốt.
- Các công cụ phổ biến: Pitest (Java), Stryker (JS/TS, C#, Scala), MutPy (Python).

---

---

## 6. Tài liệu tham khảo
1. [Stryker Mutator - Mutant states and metrics](https://stryker-mutator.io/docs/mutation-testing-elements/mutant-states-and-metrics/)
2. [PITest - Mutation Testing for Java](https://pitest.org/)
3. Ammann, P., & Offutt, J. (2016). *Introduction to Software Testing*. Cambridge University Press.
