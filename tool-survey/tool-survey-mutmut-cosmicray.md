# Khảo sát công cụ: Mutmut và Cosmic Ray

## 1. Mục tiêu

Nghiên cứu bối cảnh, mục đích, cách hoạt động và tính năng của hai công cụ kiểm thử đột biến (Mutation Testing) phổ biến nhất trong hệ sinh thái Python là **Mutmut** và **Cosmic Ray**. Khảo sát này đóng vai trò làm tài liệu tham khảo cho seminar _Mutation Testing & Test Effectiveness_, giúp so sánh và lựa chọn công cụ phù hợp tùy theo quy mô dự án và mục tiêu kiểm thử.

---

## 2. Mutmut

### 2.1 Tổng quan công cụ

Mutmut là một công cụ kiểm thử đột biến (mutation testing) hiện đại dành cho Python. Điểm đặc trưng lớn nhất của Mutmut là tính đơn giản trong sử dụng và tối ưu hóa hiệu năng vượt trội thông qua cơ chế lưu bộ nhớ đệm (caching) thông minh. Nó được thiết kế để lập trình viên có thể tích hợp nhanh vào công việc lập trình hàng ngày mà không gặp rào cản phức tạp về mặt cấu hình.

### 2.2 Mục đích chính

- Đánh giá chất lượng và độ tin cậy thực tế của bộ test suite (chủ yếu là Unit Test).
- Phát hiện các đột biến còn sống sót (surviving mutants) để chỉ ra các lỗ hổng assertion (các dòng code tuy được chạy qua nhưng không có kiểm tra assert đúng đắn logic).
- Giúp lập trình viên cải thiện chất lượng test case thay vì chỉ chạy theo chỉ số bao phủ dòng lệnh (line coverage) thông thường.

### 2.3 Ngôn ngữ/Nền tảng hỗ trợ

- **Ngôn ngữ:** Python 3 (hỗ trợ các phiên bản Python 3 hiện đại).
- **Test runner:** Hoạt động tốt với bất kỳ công cụ chạy test nào trả về exit code tiêu chuẩn, phổ biến nhất là `pytest` và `unittest`.
- **Hệ điều hành:** Hỗ trợ tốt nhất trên macOS và Linux. Trên Windows, Mutmut vẫn có thể hoạt động nhưng các tính năng đa tiến trình (multiprocessing) hoặc giao diện tương tác CLI đôi khi cần cấu hình bổ sung hoặc chạy qua WSL (Windows Subsystem for Linux) để đạt hiệu năng tối ưu.

### 2.4 Cách công cụ hoạt động

Mutmut hoạt động theo quy trình AST-based (Abstract Syntax Tree):

1. **Phân tích cú pháp:** Đọc mã nguồn Python và phân tích thành cây cú pháp trừu tượng (AST).
2. **Tạo đột biến:** Áp dụng các toán tử đột biến trực tiếp trên AST (ví dụ: thay đổi toán tử so sánh, thay đổi giá trị số, đảo ngược Boolean logic).
3. **Thực thi và lưu cache:** Chạy bộ test suite đối với mỗi đột biến được tạo ra. Kết quả chạy (Killed / Survived / Suspended / Timeout) được lưu vào file cơ sở dữ liệu SQLite cục bộ `.mutmut-cache`.
4. **Kiểm thử tăng dần (Incremental run):** Trong các lần chạy sau, Mutmut đối chiếu mã nguồn và cấu hình; nó chỉ tạo và chạy đột biến cho các tệp hoặc dòng mã đã bị thay đổi, giúp tiết kiệm tối đa thời gian.

### 2.5 Tính năng chính

- **Kiểm thử tăng dần (Incremental Testing):** Chỉ chạy lại các mutant liên quan đến phần code mới sửa đổi bằng cách sử dụng file bộ đệm `.mutmut-cache`.
- **Đột biến theo hướng bao phủ (Coverage-guided mutation):** Kết hợp với dữ liệu thu thập từ thư viện `coverage` để chỉ tạo đột biến trên những dòng code thực tế đã được test suite chạy qua, giảm thiểu thời gian kiểm thử dư thừa.
- **Giao diện tương tác terminal (`mutmut browse`):** Dashboard dạng text cho phép duyệt qua từng mutant, xem chi tiết dòng code bị thay đổi, xem lý do sống sót và kích hoạt chạy lại hoặc áp dụng trực tiếp lên file code.
- **Áp dụng đột biến lên ổ đĩa (Apply mutant to disk):** Cho phép ghi đè file đột biến lên thư mục làm việc thực tế để lập trình viên chạy thử thủ công và debug xem vì sao bộ test không bắt được lỗi.
- **Kết xuất báo cáo HTML:** Sinh báo cáo giao diện web trực quan, tô màu chi tiết các đột biến còn sống sót để dễ theo dõi.

### 2.6 Trường hợp sử dụng phổ biến

- Lập trình viên Python chạy cục bộ (local) trong quá trình phát triển các module xử lý logic quan trọng (thuật toán, tính toán tài chính, nghiệp vụ cốt lõi).
- Tích hợp vào quy trình CI/CD pipelines để kiểm soát chất lượng mã nguồn đóng góp thông qua điểm số đột biến (mutation score).

### 2.7 Điểm mạnh

- **Cực kỳ dễ sử dụng:** Cài đặt nhanh qua `pip install mutmut`, cấu hình tối giản (thường tự chạy mà không cần setup trước).
- **Tốc độ nhanh:** Nhờ cơ chế bộ nhớ đệm SQLite và tính năng chỉ mutate dòng code có độ bao phủ (coverage-guided).
- **Trải nghiệm gỡ lỗi tốt:** Lệnh `mutmut browse` và khả năng ghi đè mutant ra file thực tế giúp lập trình viên tìm ra nguyên nhân test suite yếu một cách nhanh chóng.

### 2.8 Giới hạn

- Chạy tuần tự đơn tiến trình theo mặc định, có thể gây mất nhiều thời gian ở các dự án lớn nếu không tận dụng tính năng giới hạn phạm vi thư mục.
- Vẫn tạo ra một số lượng nhất định các đột biến tương đương (equivalent mutants - đột biến thay đổi code nhưng không thay đổi hành vi thực tế của chương trình), gây mất thời gian đánh giá thủ công.
- Hỗ trợ chạy đa tiến trình song song trên Windows thuần túy có thể gặp lỗi phân luồng (forking issues).

### 2.9 Chi phí/Giấy phép

- **Chi phí:** Hoàn toàn miễn phí.
- **Giấy phép:** Mã nguồn mở, phát hành dưới giấy phép **BSD 3-Clause License**.

### 2.10 Hỗ trợ AI, nếu có

- Bản thân Mutmut là công cụ phân tích tĩnh và động truyền thống, không tích hợp sẵn các mô hình AI.
- **Ứng dụng phối hợp AI:** Kết quả xuất từ tệp bộ đệm SQLite `.mutmut-cache` hoặc báo cáo HTML rất phù hợp để làm dữ liệu đầu vào (prompt) cho các AI coding assistants (như Claude, ChatGPT, Cursor). AI có thể nhanh chóng:
  - Giải thích tại sao một mutant cụ thể lại sống sót.
  - Tự động sinh ra các unit test bổ sung để tiêu diệt (kill) mutant đó.
  - Phân tích và dự đoán xem một mutant sống sót có phải là mutant tương đương (equivalent mutant) hay không.

### 2.11 Tài liệu tham khảo

- Tài liệu chính thức (Read the Docs): [https://mutmut.readthedocs.io/](https://mutmut.readthedocs.io/)
- Mã nguồn GitHub: [https://github.com/boxed/mutmut](https://github.com/boxed/mutmut)

---

## 3. Cosmic Ray

### 3.1 Tổng quan công cụ

Cosmic Ray là một khung kiểm thử đột biến (mutation testing framework) lâu đời dành cho Python. Khác với triết lý tối giản của Mutmut, Cosmic Ray được thiết kế theo dạng mô-đun (modular) với kiến trúc plugin mạnh mẽ, hướng tới khả năng cấu hình chi tiết, độ bao phủ toán tử rộng và khả năng thực thi phân tán (distributed execution) trên các hệ thống máy chủ lớn.

### 3.2 Mục đích chính

- Thực hiện kiểm thử đột biến một cách toàn diện và có hệ thống trên toàn bộ cấu trúc mã nguồn.
- Cung cấp một nền tảng mở rộng cho phép các nhà nghiên cứu và lập trình viên chuyên nghiệp tùy biến các toán tử đột biến.
- Giải quyết bài toán hiệu năng của mutation testing bằng cách chia nhỏ công việc và chạy phân tán trên nhiều vi xử lý hoặc nhiều máy trạm.

### 3.3 Ngôn ngữ/Nền tảng hỗ trợ

- **Ngôn ngữ:** Python 3.
- **Nền tảng:** Chạy tốt trên các môi trường Linux, macOS và Windows. Tích hợp tốt nhất với `pytest` và hỗ trợ các công cụ kiểm thử chuẩn của Python.
- **Hệ thống phân tán:** Hỗ trợ tích hợp với hệ thống hàng đợi công việc (job queue) như Celery để phân phối tác vụ.

### 3.4 Cách công cụ hoạt động

Cosmic Ray hoạt động dựa trên quy trình quản lý phiên làm việc (Session-based) và lưu trữ dữ liệu tập trung:

1. **Cấu hình:** Sử dụng tệp cấu hình TOML để định nghĩa phạm vi kiểm thử, lệnh chạy test và các toán tử muốn sử dụng.
2. **Khởi tạo (`init`):** Sử dụng thư viện `parso` phân tích cú pháp mã nguồn thành AST, sinh ra toàn bộ danh sách đột biến tiềm năng và lưu vào tệp cơ sở dữ liệu SQLite (`session.sqlite`). Tệp này đóng vai trò là "kế hoạch làm việc" (work plan).
3. **Kiểm tra gốc (`baseline`):** Chạy thử bộ test suite trên mã nguồn gốc chưa đột biến để đảm bảo mọi thứ vượt qua bình thường trước khi tiến hành đột biến.
4. **Thực thi đột biến (`exec`):** Lấy từng đột biến từ file SQLite, áp dụng lên mã nguồn và chạy test. Việc thực thi có thể thông qua distributor cục bộ hoặc gửi qua mạng tới các worker của Celery. Trạng thái của từng đột biến (Killed, Survived, Incompetent, Timeout) liên tục được cập nhật lại vào tệp SQLite.
5. **Báo cáo:** Đọc tệp SQLite và xuất ra báo cáo định dạng văn bản hoặc HTML.

### 3.5 Tính năng chính

- **Kiến trúc phân tán (Distributed Execution):** Hỗ trợ cơ chế phân tán công việc (thông qua các distributor plugins như Celery hoặc HTTP) giúp chạy hàng nghìn đột biến song song trên nhiều máy trạm hoặc lõi CPU khác nhau.
- **Quản lý phiên làm việc bền vững (Session-based SQLite):** Lưu toàn bộ tiến trình vào SQLite DB, giúp chạy các tác vụ kéo dài nhiều ngày mà không sợ mất dữ liệu khi gặp sự cố ngắt điện hay crash giữa chừng. Người dùng có thể dừng (pause) và tiếp tục (resume) bất kỳ lúc nào.
- **Hệ thống toán tử đột biến phong phú:** Cung cấp nhiều toán tử đột biến tác động sâu vào cú pháp AST (thay thế toán tử, xóa decorator, nuốt ngoại lệ, thay đổi tham số hàm).
- **Khả năng mở rộng cao:** Thiết kế dựa trên hệ thống plugin cho phép lập trình viên tự định nghĩa thêm các toán tử đột biến mới hoặc bộ phân phối test case mới.

### 3.6 Trường hợp sử dụng phổ biến

- Các dự án Python quy mô lớn, doanh nghiệp có hạ tầng CI/CD mạnh hoặc hệ thống máy tính phân tán.
- Các nghiên cứu khoa học, học thuật về Mutation Testing cần trích xuất số liệu phân tích chi tiết (thông qua việc truy vấn trực tiếp cơ sở dữ liệu SQLite của phiên làm việc).

### 3.7 Điểm mạnh

- **Khả năng mở rộng cực tốt:** Thích hợp cho các dự án khổng lồ nhờ cơ chế phân tán.
- **Độ tin cậy của tiến trình cao:** Cơ sở dữ liệu SQLite lưu vết chi tiết đảm bảo không bị mất tiến độ chạy.
- **Độ chính xác cao:** Phân tích AST sâu và chính xác bằng cách sử dụng parser chất lượng cao (`parso`).

### 3.8 Giới hạn

- **Độ phức tạp cấu hình cao:** Quy trình sử dụng yêu cầu thực hiện nhiều lệnh tuần tự (`new-config` -> `init` -> `baseline` -> `exec`), tạo ra rào cản cho người mới bắt đầu.
- **Chi phí thiết lập phân tán lớn:** Việc cài đặt Celery và các message broker đi kèm (Redis/RabbitMQ) đòi hỏi kiến thức vận hành hệ thống.
- **Tốc độ chạy đơn nhân chậm:** Nếu chạy cục bộ trên một máy tính bình thường không qua cấu hình song song phức tạp, Cosmic Ray có tốc độ kém tối ưu hơn Mutmut do thiếu cơ chế incremental cache thông minh cho các file không đổi.
- Tần suất cập nhật phiên bản mới và cộng đồng hỗ trợ hiện tại có phần kém năng động hơn so với Mutmut.

### 3.9 Chi phí/Giấy phép

- **Chi phí:** Hoàn toàn miễn phí.
- **Giấy phép:** Mã nguồn mở, phát hành dưới giấy phép **BSD 2-Clause License**.

### 3.10 Hỗ trợ AI, nếu có

- Cosmic Ray không tích hợp sẵn bất kỳ module AI nào.
- **Ứng dụng phối hợp AI:** Cấu trúc dữ liệu lưu trong file SQLite của Cosmic Ray rất tường minh và chi tiết. Lập trình viên hoặc các hệ thống CI/CD tự động có thể sử dụng AI để đọc trực tiếp schema SQLite này, thực hiện các phân tích thống kê tự động và đề xuất viết code/test hiệu quả hơn cho những file có tỉ lệ đột biến sống sót cao.

### 3.11 Tài liệu tham khảo

- Tài liệu chính thức (Read the Docs): [https://cosmic-ray.readthedocs.io/](https://cosmic-ray.readthedocs.io/)
- Mã nguồn GitHub: [https://github.com/sixty-north/cosmic-ray](https://github.com/sixty-north/cosmic-ray)
