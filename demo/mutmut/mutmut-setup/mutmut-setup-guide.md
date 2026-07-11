# Bắt đầu với Mutmut:

Hướng dẫn này cung cấp một phương pháp tiếp cận có cấu trúc để thiết lập và chạy kiểm thử đột biến (mutation testing) trên dự án Python của bạn bằng cách sử dụng [Mutmut](https://github.com/boxed/mutmut).

## Điều kiện
- Môi trường Python (khuyên dùng: sử dụng môi trường ảo - virtual environment).
- Một dự án có bộ kiểm thử (thường sử dụng `pytest`).

## Bước 1: Cài đặt
1.  **Tạo môi trường ảo**:
    Việc cô lập môi trường kiểm thử đột biến của bạn là phương pháp thực hành tốt nhất.
    ```bash
    python3 -m venv mutmut_env
    source mutmut_env/bin/activate
    ```

2.  **Cài đặt Mutmut**:
    ```bash
    pip install mutmut
    ```

## Bước 2: Cấu hình dự án
Mutmut cần biết mã nguồn của bạn nằm ở đâu để tạo ra các đột biến (mutants).
1.  **Cấu hình `pyproject.toml` hoặc `setup.cfg`**:
    Đảm bảo rằng bạn đã xác định thư mục mã nguồn. Ví dụ: nếu mã của bạn nằm trong thư mục `src/`, hãy thêm đoạn sau vào tệp `pyproject.toml` của bạn:
    ```toml
    [tool.mutmut]
    source_paths = ["src/"]
    pytest_add_cli_args_test_selection = ["tests/"]
    ```

## Bước 3: Chạy kiểm thử đột biến
Sau khi cấu hình xong, bạn có thể chạy các bài kiểm thử đột biến.

1.  **Chạy kiểm thử**:
    ```bash
    mutmut run
    ```
    *Lưu ý: Nếu bạn gặp sự cố với đường dẫn import hoặc trạng thái môi trường, hãy đảm bảo rằng bạn đã xóa các tệp bộ nhớ tạm (cache) trước đó:*
    ```bash
    rm -rf mutants/ .mutmut-cache/ .coverage
    find . -type d -name "__pycache__" -exec rm -rf {} +
    find . -type f -name "*.pyc" -delete
    ```

2.  **Theo dõi tiến độ**:
    Mutmut sẽ hiển thị số lượng đột biến được tạo ra và trạng thái của chúng (Killed - Đã tiêu diệt, Survived - Sống sót, v.v.).

## Bước 4: Phân tích kết quả
Sau khi quá trình chạy hoàn tất, bạn có thể kiểm tra các đột biến đã sống sót (những thay đổi mã mà bộ kiểm thử của bạn không phát hiện được).

1.  **Duyệt xem kết quả**:
    ```bash
    mutmut browse
    ```
    Lệnh này sẽ khởi chạy một công cụ cho phép bạn xem chính xác những dòng nào đã bị đột biến và lý do tại sao các bài kiểm thử vẫn pass (vượt qua) bất chấp sự thay đổi đó.

## Mẹo khắc phục sự cố
- **ModuleNotFoundError**: Đảm bảo `PYTHONPATH` của bạn bao gồm thư mục mã nguồn hoặc dự án của bạn đã được cài đặt ở chế độ có thể chỉnh sửa (`pip install -e .`).
- **Lỗi Trampoline/Import**: Nếu bạn gặp lỗi liên quan đến tên mô-đun (như `src.`), hãy đảm bảo các import trong bài kiểm thử của bạn khớp với cấu trúc mà trình chạy kiểm thử mong đợi.
- **Dọn dẹp**: Luôn xóa các thư mục `mutants/` và `.mutmut-cache/` trước một lần chạy mới nếu bạn đã thay đổi cấu hình dự án hoặc các thư viện phụ thuộc.