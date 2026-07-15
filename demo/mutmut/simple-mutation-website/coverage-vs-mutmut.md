# Phân tích tương quan giữa Coverage và Mutation Score

Phạm vi: Các hàm trong `Datastore` của [Website Điện tử Python.](https://github.com/darumor/simple-python-website.git)

Công cụ: Coverage qua `coverage.py` và mutation testing từ Mutmut.

## 1. Bảng số liệu

| Chỉ số | Trước integrate | Sau integrate | Δ |
|---|---:|---:|---:|
| **Average coverage** | **61%** | **88%** | **+27%** |
| `connection` coverage | 77% | 77% | - |
| `store` coverage | 91% | 91% | - |
| `things` coverage | 0% | 100% | +100% |
| `users` coverage | 18% | 89% | +71% |
| Missed Lines Count | 55 | 17 | -38 |
| Mutation score (killed-only/total) | 46.08% | 93.95% | +47.87% |
| Mutants Killed | 94 | 202 | +108 |
| Mutants Total | 204 | 215 | +11 |

## 2. Phân tích trước Integrate:
Tương quan: Coverage trung bình 61% nhưng mutation score chỉ đạt 46.08%.

Tập test demo ban đầu mang tính chất "khởi tạo" (bootstrap), tập trung vào các luồng tích cực đơn giản của `connection` và `store`. Tuy nhiên, các phần cốt lõi xử lý logic dữ liệu trong `users` và `things` bị bỏ ngỏ hoặc chỉ được thực thi một phần nhỏ:

* **Lỗ hổng "Coverage giả tạo":** Các hàm trong `users` có coverage 18% nhưng mutation score rất thấp. Ví dụ: các dòng khởi tạo kết nối database được thực thi (nằm trong `coverage`), nhưng các mutant thay đổi toán tử logic hoặc hằng số trả về vẫn "sống sót" vì các test case thiếu `assert` kiểm tra giá trị đầu ra.
* **Điểm mù nghiêm trọng:** Module `things` có coverage 0%, đồng nghĩa với việc toàn bộ logic nghiệp vụ tại đây nằm ngoài tầm kiểm soát của test, tạo ra một vùng trống lớn mà coverage truyền thống không thể cảnh báo mức độ rủi ro thực tế.

## 3. Phân tích sau Integrate

Tương quan: Coverage 88% và mutation score 93.95%.

Sau khi bổ sung class test chuyên biệt để phủ kín logic của `users` và `things`, bức tranh thay đổi rõ rệt:

* **Sự hội tụ:** Khoảng cách giữa Coverage (88%) và Mutation Score (93.95%) trở nên rất hẹp. Việc tập trung kiểm thử vào các hàm xử lý dữ liệu phức tạp giúp các `assert` bám sát vào hành vi thay vì chỉ "chạy cho qua" code.
* **Chất lượng test:** Số lượng mutant bị tiêu diệt tăng vọt (+108) cho thấy các test mới không chỉ đơn thuần bao phủ các dòng code (tăng coverage) mà thực sự có khả năng phát hiện lỗi.
* **Bài học:** Việc đạt được 100% coverage ở module `things` và cải thiện 71% coverage ở `users` trực tiếp dẫn đến việc tăng mạnh độ tin cậy của hệ thống. Những mutant còn sót lại (khoảng 6%) chủ yếu nằm ở các trường hợp cạnh tranh (edge cases) hoặc các thuộc tính không ảnh hưởng trực tiếp đến kết quả thực thi, khẳng định rằng khi đã có độ bao phủ cao, mutation testing trở thành công cụ quan trọng để tinh chỉnh những lỗi logic tinh vi nhất trong hệ thống.