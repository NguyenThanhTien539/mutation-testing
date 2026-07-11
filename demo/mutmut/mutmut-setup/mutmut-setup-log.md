# Báo cáo Dự án Kiểm thử Đột biến (Mutmut)

### Giai đoạn 1: Fork kho lưu trữ Mutmut chính thức và thiết lập tất cả các mô-đun cần thiết
- Đã fork từ https://github.com/boxed/mutmut.git
- Đã hoàn tất cài đặt Ubuntu/Linux (Ubuntu-Storage)
- Đã đọc kế hoạch trong README và tạo kế hoạch này.

### Giai đoạn 2: Cài đặt các thư viện và chạy Mutmut
- Đã tạo một môi trường ảo để cài đặt bằng cách sử dụng `python3`.
- Đã cài đặt tất cả các thư viện cần thiết được cung cấp trong `pyproject.toml`.
- Đã gỡ lỗi và cập nhật tất cả các thư viện lên phiên bản mới nhất để giải quyết các lỗi import ban đầu.
- Đã xác nhận rằng Mutmut đang hoạt động bằng cách sử dụng lệnh `mutmut run` trong môi trường ảo.

### Giai đoạn 3: Thiết lập một bài kiểm thử đơn giản
- Đã tạo một thư mục riêng (`python_test`) với tệp `calculator.py` và tệp `tests/test_calculator.py`.
- Đã cấu hình cấu trúc dự án để giải quyết lỗi `ModuleNotFoundError` bằng cách đảm bảo việc lồng thư mục và import gói (package) phù hợp.
- Các bài kiểm thử ban đầu bị thất bại do không khớp import và lỗi trampoline (liên quan đến việc xử lý tiền tố `src.`); những vấn đề này đã được giải quyết bằng cách dọn dẹp các tệp `__pycache__` và `.pyc`, đồng thời điều chỉnh các đường dẫn import trong kiểm thử.
- Đã chạy `mutmut run` trên thư mục để thực hiện kiểm thử đột biến.

### Giai đoạn 4: Tài liệu hóa kết quả
- Kết quả đã được theo dõi thông qua đầu ra của lệnh `mutmut run` và công cụ tiện ích `mutmut browse`.
- Đã giải quyết các vấn đề về cấu hình bằng cách dọn dẹp các tệp bộ nhớ tạm (`mutants/`, `.mutmut-cache/`, `.coverage`) giữa các lần chạy.
- Kết quả kiểm thử đột biến cuối cùng:
    - **Tổng số đột biến (Total Mutants)**: 108
    - **Đã tiêu diệt (Killed - 🎉)**: 2
    - **Chưa kiểm thử (Untested - 🫥)**: 106
    - **Hiệu suất (Performance)**: 1.93 đột biến/giây (mutations/second)