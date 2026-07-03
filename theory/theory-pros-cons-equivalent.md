# Equivalent Mutants và các giới hạn

## 1. Mục tiêu

Nghiên cứu sâu về khái niệm **Equivalent Mutants** (Mutant tương đương) trong Mutation Testing (Kiểm thử đột biến), giải thích nguyên nhân tại sao một số mutant không thể bị tiêu diệt (killed), đồng thời phân tích các giới hạn cốt lõi và thách thức về mặt hiệu năng (chi phí, tốc độ) của phương pháp kiểm thử này.

## 2. Câu hỏi chính

- **Equivalent mutant là gì?**
- **Vì sao một số mutant survived nhưng không thể bị killed?**
- **Các giới hạn của Mutation Testing là gì?**
- **Vì sao Mutation Testing có thể tốn kém hoặc chạy chậm?**

## 3. Ghi chú chính

### 3.1. Khái niệm Equivalent Mutant (Mutant tương đương)

Trong Mutation Testing, một **Equivalent Mutant** là một phiên bản mã nguồn bị biến đổi (mutant) có cú pháp khác với chương trình gốc nhưng lại có **hành vi ngữ nghĩa (semantic behavior) hoàn toàn trùng khớp** với chương trình gốc.

- Mặc dù mã nguồn thay đổi, nhưng với mọi bộ dữ liệu đầu vào có thể (đúng cú pháp hoặc sai cú pháp), mutant này đều trả về kết quả cấu trúc, trạng thái nội tại và đầu ra y hệt chương trình gốc.
- **Hệ quả:** Do hành vi không đổi, không một ca kiểm thử (test case) nào – dù được thiết kế tốt đến đâu – có thể phân biệt được mutant này với chương trình gốc. Vì vậy, loại mutant này không bao giờ có thể bị "killed" (tiêu diệt) mà sẽ luôn "survived" (sống sót).

### 3.2. Vì sao một số mutant survived nhưng không thể bị killed?

Có hai nguyên nhân chính khiến một mutant sống sót mà không thể bị tiêu diệt:

1. **Bản chất là Equivalent Mutant (Nguyên nhân phổ biến nhất):**
   Như đã định nghĩa ở trên, do thuật toán hoặc biểu thức logic sau khi đột biến có tính chất tương đương toán học hoặc tương đương logic với đoạn mã gốc, hành vi của hệ thống không hề thay đổi. Do đó, kiểm thử không thể phát hiện sai lệch.
2. **Mã chết hoặc Mã không thể chạm tới (Dead Code / Unreachable Code):**
   Nếu toán tử đột biến tác động vào một phân đoạn mã nguồn không bao giờ được thực thi trong thực tế (ví dụ: một khối `catch` không bao giờ xảy ra, một điều kiện luôn luôn sai `if (false)` kế thừa từ logic khác, hoặc mã tối ưu hóa dư thừa), thì sự thay đổi đó không ảnh hưởng đến luồng chạy chính của chương trình. Vì mã không chạy qua, test case không thể kích hoạt (trigger) lỗi để bắt được mutant đó.
3. **Thiếu khả năng quan sát trạng thái (Lack of Observability):**
   Đột biến làm thay đổi trạng thái bên trong của đối tượng, nhưng trạng thái này là `private` và không có cơ chế nào (như hàm getter, log, hoặc trả về qua hàm) để test case kiểm tra và khẳng định sự thay đổi. Chương trình vẫn kết thúc thành công và trả về đầu ra đúng, khiến mutant sống sót.

### 3.3. Các giới hạn của Mutation Testing

Mặc dù Mutation Testing là một kỹ thuật cực kỳ mạnh mẽ để đánh giá chất lượng của bộ test case, nó vẫn vấp phải các giới hạn nghiêm trọng:

- **Bài toán Mutant Tương đương (The Equivalent Mutant Problem):** Việc xác định một mutant có phải là tương đương hay không là một bài toán **không thể giải quyết một cách tổng quát bằng máy tính** (Undecidable Problem - tương tự bài toán dừng Halting Problem). Hiện nay, lập trình viên thường phải rà soát bằng tay (manual review) từng mutant sống sót để xem nó là do bộ test yếu hay do nó là equivalent mutant. Quá trình này tốn rất nhiều thời gian và công sức.
- **Sự bùng nổ tổ hợp (Combinatorial Explosion):**
  Số lượng mutant sinh ra tỷ lệ thuận với số lượng dòng mã và số lượng toán tử đột biến (mutation operators). Với các hệ thống lớn hàng triệu dòng code, số lượng mutant có thể lên tới hàng trăm nghìn hoặc hàng triệu, khiến việc quản lý và thực thi trở nên quá tải.
- **Tỷ lệ nhiễu cao (High Noise Rate):**
  Lập trình viên dễ bị nản lòng khi thấy Mutation Score (điểm đột biến) thấp, nhưng khi kiểm tra thì phần lớn mutant sống sót lại là các equivalent mutants chứ không phải do họ viết thiếu test case.
- **Phụ thuộc vào Công cụ (Tooling Dependency):**
  Mỗi ngôn ngữ lập trình cần có công cụ Mutation Testing riêng biệt (ví dụ: Pitest cho Java, Stryker cho JS/C#, MutPy cho Python). Một số ngôn ngữ chưa có công cụ tối ưu hoặc công cụ chạy rất thiếu ổn định.

### 3.4. Vì sao Mutation Testing có thể tốn kém hoặc chạy chậm?

Chi phí tài nguyên và thời gian là rào cản lớn nhất khiến Mutation Testing chưa được áp dụng phổ biến trong mọi chu trình CI/CD tự động. Nguyên nhân bao gồm:

- **Khối lượng thực thi khổng lồ (Massive Execution Cost):**
  Giả sử một dự án có $N$ mutants và bộ test suite có $T$ test cases. Trong trường hợp xấu nhất, hệ thống sẽ phải chạy lại $N 	imes T$ lần kiểm thử. Dù các công cụ hiện đại có tối ưu bằng cách chỉ chạy các test case có đi qua vùng mã bị đột biến (Test Filtering), số lần chạy lại vẫn là một con số rất lớn.
- **Chi phí biên dịch và khởi động (Compilation & Setup Overhead):**
  Đối với các ngôn ngữ biên dịch (Java, C++, C#), mỗi mutant có thể yêu cầu công cụ phải biên dịch lại một phần mã nguồn hoặc sửa đổi bytecode/AST trong bộ nhớ, sau đó khởi động lại ngữ cảnh kiểm thử (như Spring Context, Database Mock), chu kỳ này lặp đi lặp lại hàng ngàn lần gây lãng phí tài nguyên CPU và RAM.
- **Chi phí nhân lực (Human Cost):**
  Việc phân tích các mutant sống sót đòi hỏi các kỹ sư có trình độ cao ngồi đọc lại mã nguồn, hiểu sâu về logic để phân loại, gây tốn kém chi phí vận hành doanh nghiệp.

## 4. Ví dụ

Xét phép đột biến đổi biểu thức toán học từ: `a + b` thành `b + a`.

### Phân tích ngữ nghĩa:

- Trong toán học và hầu hết các ngôn ngữ lập trình (với các kiểu dữ liệu số như `int`, `float`, `double`), phép cộng có **tính chất giao hoán (Commutative Property)**.
- Nghĩa là với mọi giá trị của `a` và `b`, kết quả của `a + b` luôn luôn bằng `b + a`.

### Kết luận kiểm thử:

Cho dù bạn có viết bao nhiêu test case, truyền vào các giá trị biên, giá trị âm, hay giá trị bằng 0, thì chương trình gốc và mutant này đều trả về một kết quả đầu ra giống nhau 100%. Không có một khẳng định kiểm thử (`assert`) nào có thể kích hoạt sự sai lệch hành vi để giết chết mutant này.

Do đó, sự thay đổi từ `a + b` sang `b + a` đối với kiểu số là một ví dụ điển hình của một **Equivalent Mutant**.

_Lưu ý mở rộng:_ Phép toán này có thể KHÔNG tương đương nếu `a` và `b` là kiểu chuỗi (String) ở một số ngôn ngữ (vì `"A" + "B"` = `"AB"`, trong khi `"B" + "A"` = `"BA"`), hoặc nếu việc đánh giá `a` hoặc `b` sinh ra hiệu ứng phụ (Side Effect) theo thứ tự gọi hàm. Nhưng trong ngữ cảnh toán học thuần túy, chúng hoàn toàn tương đương.

## 5. Ý chính cần ghi nhớ

1. **Equivalent Mutant** đổi cú pháp nhưng giữ nguyên ngữ nghĩa. Nó không bao giờ bị giết bởi bất kỳ test case nào.
2. Việc nhận diện Equivalent Mutant là một bài toán **Undecidable**, hiện tại vẫn phải dựa nhiều vào nhân lực để thẩm định thủ công.
3. **Mutation Testing chậm** vì nó nhân số lượng mutant với số lượng test case, đòi hỏi năng lực máy tính cực kỳ lớn.
4. Để tối ưu Mutation Testing trong thực tế, người ta áp dụng các kỹ thuật như **Tối ưu hóa Bytecode**, **Đột biến cấp cao (Extreme Mutation)**, và chỉ chạy Mutation Testing trên các nhánh mã nguồn thay đổi (Incremental Mutation Testing) thay vì toàn bộ hệ thống.

## 6. Tài liệu tham khảo

- Offutt, A. J., & Pan, J. (1997). _Automatically detecting equivalent mutants_. Software Testing, Verification and Reliability, 7(3), 165-192. [DOI: 10.1002/...3.0.CO;2-U](<https://doi.org/10.1002/(SICI)1099-1689(199709)7:3%3C165::AID-STVR143%3E3.0.CO;2-U>)
- Jia, Y., & Harman, M. (2011). _An analysis and survey of mutation testing_. IEEE Transactions on Software Engineering, 37(5), 649-678. [DOI: 10.1109/TSE.2010.62](https://doi.org/10.1109/TSE.2010.62)
- Pitest Documentation. _Basic Concepts - Equivalent Mutations_. [Truy cập tại pitest.org](https://pitest.org/quickstart/basic_concepts/#equivalent-mutations)
