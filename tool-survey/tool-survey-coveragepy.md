# Khảo sát công cụ: Coverage.py

## 1. Mục tiêu

Nghiên cứu bối cảnh, mục đích và cách sử dụng Coverage.py — công cụ đo lường code coverage tiêu chuẩn cho hệ sinh thái Python — phục vụ seminar **Mutation Testing & Test Effectiveness**. Coverage.py đóng vai trò tương đương Istanbul/nyc (JavaScript) và JaCoCo (Java) đã khảo sát trước đó, nhưng dành riêng cho Python, đồng thời là nền tảng dữ liệu mà chính Mutmut sử dụng cho cơ chế coverage-guided mutation (đã đề cập ở `tool-survey-mutmut-cosmicray.md`).

## 2. Coverage.py

### 2.1 Tổng quan công cụ

Coverage.py là thư viện đo lường độ bao phủ mã nguồn (code coverage) tiêu chuẩn công nghiệp cho Python, do Ned Batchelder phát triển và duy trì từ năm 2004. Đây **không phải** công cụ mutation testing, mà là công cụ đo coverage thuần tuý — tương tự Istanbul/nyc và JaCoCo, chỉ khác ngôn ngữ mục tiêu.

### 2.2 Mục đích chính

Theo dõi, đo lường và báo cáo tỷ lệ phần trăm mã nguồn Python thực sự được thực thi trong quá trình chạy test (Unit Test, Integration Test). Mục đích cuối cùng là giúp lập trình viên tìm ra những đoạn code chưa từng được test chạy qua ("dead code" hoặc thiếu test case) — đúng vai trò "ranh giới dưới" (Lower Bound) đã trình bày ở `theory-coverage-vs-mutation.md`.

### 2.3 Ngôn ngữ/Nền tảng hỗ trợ

- **Ngôn ngữ:** Python 3 (các bản Coverage.py mới nhất hỗ trợ từ Python 3.9 trở lên; các bản cũ hơn còn hỗ trợ Python 2.7).
- **Test runner:** Chạy độc lập qua CLI `coverage run`, hoặc tích hợp trực tiếp vào `pytest` thông qua plugin `pytest-cov`; cũng tương thích `unittest`, `nose2`.
- Từ Python 3.12, Coverage.py có thể tận dụng cơ chế `sys.monitoring` (PEP 669) để giảm đáng kể overhead so với cơ chế `sys.settrace` truyền thống dùng ở các phiên bản Python cũ hơn.

### 2.4 Cách công cụ hoạt động

Coverage.py hoạt động dựa trên cơ chế theo dõi thực thi (execution tracing):

1. Khi chạy `coverage run my_script.py` (hoặc `pytest --cov`), Coverage.py gắn một tracer vào trình thông dịch Python.
2. Tracer ghi lại mỗi dòng lệnh — và tuỳ chọn cả nhánh rẽ (branch) — được thực thi trong quá trình chạy.
3. Dữ liệu thực thi được lưu vào file nhị phân `.coverage`.
4. Sau khi chạy xong, các lệnh `coverage report`, `coverage html`, `coverage xml`, `coverage json` đọc file này và xuất báo cáo theo định dạng tương ứng.

Ví dụ sử dụng cơ bản:

```bash
pip install coverage
coverage run -m pytest
coverage report -m
coverage html
```

### 2.5 Tính năng chính

- Đo lường **Statement Coverage** và **Branch Coverage** (branch coverage cần bật tường minh bằng `branch = True` trong cấu hình).
- Hỗ trợ file cấu hình `.coveragerc` hoặc mục `[tool.coverage.run]` trong `pyproject.toml`.
- `--source`, `--include`, `--omit` để giới hạn phạm vi đo lường.
- `# pragma: no cover` để loại trừ những dòng code không cần đo (ví dụ code chỉ chạy khi debug).
- `coverage combine` để gộp dữ liệu coverage từ nhiều tiến trình song song hoặc nhiều lần chạy trong CI matrix.
- **Dynamic contexts**: gắn nhãn "test nào đã chạy qua dòng code nào", hữu ích khi truy vết nguyên nhân.
- `fail_under` trong cấu hình để tự động fail nếu coverage thấp hơn ngưỡng đặt ra.
- Xuất báo cáo nhiều định dạng: text, HTML (có highlight dòng chưa chạy), XML (tương thích Cobertura), JSON, LCOV.

### 2.6 Trường hợp sử dụng phổ biến

- Đo coverage cho Python project trong CI/CD (GitHub Actions, GitLab CI) làm Quality Gate trước khi merge Pull Request.
- **Chạy trước khi áp dụng Mutmut hoặc Cosmic Ray**: cả hai công cụ mutation testing này đều đọc dữ liệu từ Coverage.py để giới hạn phạm vi mutate vào những dòng đã có test chạy qua (coverage-guided mutation), giúp giảm đáng kể thời gian chạy.
- Kết hợp `pytest-cov` để đo coverage ngay trong lệnh test hằng ngày của lập trình viên Python.

### 2.7 Điểm mạnh

- Tiêu chuẩn công nghiệp (de-facto standard) cho hệ sinh thái Python, được duy trì liên tục hơn 20 năm.
- Cài đặt và cấu hình đơn giản, tích hợp liền mạch với `pytest` qua `pytest-cov`.
- Hỗ trợ cả Statement và Branch coverage, không chỉ dừng ở statement như một số tool coverage khác.
- Report HTML trực quan, dễ đọc, có highlight từng dòng.
- Từ Python 3.12, overhead đo lường giảm mạnh nhờ `sys.monitoring`.
- Là nền tảng dữ liệu giúp các công cụ mutation testing Python (đặc biệt là Mutmut) hoạt động hiệu quả hơn.

### 2.8 Giới hạn

- Chỉ đo được việc dòng code có chạy qua hay không, **không xác minh assertion có đúng logic hay không** — đúng giới hạn chung của mọi coverage tool đã nêu ở `theory-coverage-vs-mutation.md`.
- Branch coverage không bật mặc định; dễ gây ngộ nhận đã đo branch coverage trong khi thực chất chỉ đang đo statement coverage nếu quên cấu hình `branch = True`.
- Khi chạy đa tiến trình (multiprocessing, `pytest-xdist`), cần thêm bước `coverage combine` thủ công, dễ bị bỏ sót khiến báo cáo coverage bị thiếu dữ liệu.
- Không phải công cụ mutation testing — không đo được Test Effectiveness theo đúng nghĩa lý thuyết đã trình bày ở `theory-test-effectiveness.md`.

### 2.9 Chi phí/Giấy phép

- Chi phí: Miễn phí hoàn toàn.
- Giấy phép: Mã nguồn mở, phát hành dưới giấy phép **Apache License 2.0**.

### 2.10 Hỗ trợ AI, nếu có

Coverage.py là công cụ phân tích tĩnh/động truyền thống, không tích hợp AI trực tiếp. Tuy nhiên, dữ liệu XML/JSON xuất ra có thể làm đầu vào cho các nền tảng phân tích chất lượng có yếu tố AI (SonarQube, Codecov) để gợi ý vùng code cần bổ sung test. Đáng chú ý hơn: chính dữ liệu `.coverage` này là thứ Mutmut đọc để tự động giới hạn phạm vi mutate (coverage-guided mutation) — một dạng tối ưu hoá tự động dựa trên dữ liệu, dù bản thân Coverage.py không gắn nhãn "AI".

### 2.11 Tài liệu tham khảo

- Coverage.py official documentation: https://coverage.readthedocs.io/
- Coverage.py GitHub repository: https://github.com/nedbat/coveragepy
- pytest-cov plugin: https://pytest-cov.readthedocs.io/
