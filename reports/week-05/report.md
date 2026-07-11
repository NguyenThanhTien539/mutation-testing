# Báo Cáo Tuần - Tuần 04

## 1. Thông Tin Chung

| Mục                 | Thông tin                                                                      |
| ------------------- | ------------------------------------------------------------------------------ |
| Mã nhóm             | 02                                                                             |
| Tên đề tài          | Mutation Testing & Test Effectiveness                                          |
| Thời gian thực hiện | 2026-07-06 - 2026-07-11                                                        |
| GitHub Repository   | [[GitHub Repository] ](https://github.com/NguyenThanhTien539/mutation-testing) |

---

## 2. Công Việc Đã Hoàn Thành Trong Tuần

### [23127061] - Trương Lý Khải

#### Task: Tải về, tìm hiểu và setup công cụ Mutmut; Lập hướng dẫn cài Mutmut và setup 1 demo mẫu

- **Mô tả:** Tổng hợp lại các thông tin cơ bản về Mutmut, tìm repository tương ứng và tìm cách để sử dụng công cụ thành công. Ghi lại các bước cài đặt dependency, sử dụng công cụ và cho 1 ví dụ mẫu để thành viên khác có thể tự sử dụng Mutmut 1 cách nhanh chóng
- **Trạng thái:** Hoàn thành
- **Minh chứng:**
  - [Jira task](https://mutation-testing-seminar.atlassian.net/browse/KAN-17)
  - [Output file](https://drive.google.com/drive/folders/1Tpst2Td0uSt_cp24yk3E5YA23-Q8Za9j?usp=drive_link)
  - [Prompt log - Google Gemini](https://share.gemini.google/oi4aLPR73o6c)
- **Mục đích sử dụng AI:** Sử dụng AI để làm rõ và chỉnh sửa các lỗi nhất thống phiên bản do Mutmut đã được thay đổi nhiều so với phiên bản cũ

### [23127296] - Nguyễn Thành Luân

#### Task 1: Tổng hợp và so sánh 10 công cụ đã tìm hiểu

- **Mô tả:** tổng hợp lại các thông tin cơ bản về 10 công cụ và so sánh trên các tiêu chí như giá, ngôn ngữ, khả năng tích hợp AI,...
- **Trạng thái:** Hoàn thành
- **Minh chứng:**
  - [Jira task](https://mutation-testing-seminar.atlassian.net/browse/KAN-20)
  - [Output file](https://drive.google.com/file/d/1Z6vYNinCl4vHMbrB1FATlUNdTcvVVD5h/view?usp=drive_link)
  - Prompt - Claude (visual studio code): "Hãy kiểm tra nội dung của file tool-comparison-final.md và so sánh với nội dung của các file tìm hiểu tôi gửi xem có thống nhất không. Nếu không thì hãy báo cáo lại những sai sót."
- **Mục đích sử dụng AI:** Sử dụng AI để làm rõ và chỉnh sửa các lỗi nhất thống phiên bản do Mutmut đã được thay đổi nhiều so với phiên bản cũ

#### Task 2: Setup StrykerJS trên hệ thống Eshop

- **Mô tả:** ghi lại các bước cài đặt dependency, tạo file test và các file cấu hình trước khi chạy mutation test bằng StrykerJS trên đồ án.
- **Trạng thái:** Hoàn thành
- **Minh chứng:**
  - [Jira task](https://mutation-testing-seminar.atlassian.net/browse/KAN-15)
  - [Output file](https://drive.google.com/file/d/1jwxs2WFO6jxWLUkhn9L1NMf6A8Sfmiyq/view?usp=drive_link)
- **Sử dụng AI:** không

---

### [23127330] - Ngô An Bình

#### Task 1: Tổng hợp nội dung để làm dàn ý cho slides

- **Mô tả:** Tổng hợp nội dung chính từ các file theory và survey để xây dựng cấu trúc slides rõ ràng, logic
- **Trạng thái:** Hoàn thành
- **Minh chứng:**
  - [Jira task](https://mutation-testing-seminar.atlassian.net/browse/KAN-19)
  - [Output file](https://drive.google.com/file/d/1WNKIHxOrstWMzjfHY37vyGXtbXdZpdUi/view?usp=sharing)
  - [AI prompt](https://drive.google.com/file/d/1EYJK2Wyk40LGc8mfCl7Sh2iEmFfvZgIG/view?usp=sharing)
- **Mục đích sử dụng AI:** Gợi ý cấu trúc slide (tiêu đề, nội dung chính, speak notes, đồ họa gợi ý), trích các ý chính và tóm tắt nội dung.

---

### [23127404] - Lê Tuấn Lộc

#### Task: Viết kịch bản chạy Mutmut trên 1 demo mẫu code Python

- **Mô tả:** Sử dụng hướng dẫn cài Mutmut và tạo kịch bản và lưu kết quả chạy demo Mutmut trên 1 hệ thống calculator mẫu bằng python
- **Trạng thái:** Hoàn thành
- **Minh chứng:**
  - [Jira task](https://mutation-testing-seminar.atlassian.net/browse/KAN-18)
  - [Output file](https://drive.google.com/drive/folders/1i-taG_P859i85rQyT78xsuGpUl7aiJ-7?usp=drive_link)
- **Mục đích sử dụng AI:** Không có

---

### [23127539] - Nguyễn Thanh Tiến

- **Mô tả:** tạo kịch bản và chạy mutation test dùng StrykerJS trên 2 tính năng của hệ thống EShop, phân tích kết quả khi test có độ coverage cao và thấp.
- **Trạng thái:** Hoàn thành
- **Minh chứng:**
  - [Jira task](https://mutation-testing-seminar.atlassian.net/browse/KAN-16)
  - [Output file](https://docs.google.com/document/d/1muhH2U5mpxiLKfO-vvynbVDmptMsbntyjf7lYFPnbJo/edit?usp=sharing) (note: thư mục gồm report chứa phân tích kết quả và source code đã bao gồm test case và cấu hình StrykerJS)
  - Prompt-Claude (Visual studio code): "Hãy đọc file README.md và phân tích những chức năng có thể thực hiện mutation test. Đề xuất cách thiết kế test case cho mutation test để thấy được tầm quan trọng của coverage."
- **Mục đích sử dụng AI:** phân tích các tính năng của EShop có thể thực hiện mutation testing, hỗ trợ tạo test case để phân tích độ hiệu quả của mutation test khi test có độ coverage cao và thấp.

---

## 3. Công Việc Dự Kiến Cho Tuần Sau

Trong tuần 6, nhóm dự kiến thực hiện các công việc sau:

- Làm slide seminar trên Canva dựa theo outline đã có.
- Phân tích so sánh Test Effectiveness giữa StrykerJS và Mutmut.
- Mở rộng kịch bản test thêm các tình huống khó (equivalent mutant, logic phức tạp).
- Chuẩn bị demo project ổn định cho cả 2 công cụ.
- Review chéo slide và nội dung giữa các thành viên.
