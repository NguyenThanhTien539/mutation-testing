# Báo cáo: Đánh giá hiệu quả Test với Mutation Testing (mutmut)

## 1. Hai chức năng được test

| # | Chức năng | File source | Mô tả |
| :--- | :--- | :--- | :--- |
| 1 | **Basic arithmetic (Toán học cơ bản)** | `src/calculator/core.py` | Xử lý các phép toán số học cơ bản. Logic thuần túy, không phụ thuộc trạng thái bên ngoài. |
| 2 | **Arithmetic equation solver (Giải phương trình)** | `src/calculator/core.py` | Tìm nghiệm phương trình số học bằng phương pháp chia đôi (bisection method). Chứa logic lặp `range(100)`, điều kiện hội tụ `tolerance=1e-7` và tham số mặc định `guess=0`. |

**Lý do chọn 2 chức năng này để kiểm thử đột biến:**
- **Basic arithmetic**: Đại diện cho nhóm code đơn giản, logic tuyến tính. Đây là trường hợp lý tưởng để minh họa việc bộ test unit chuẩn xác có thể dễ dàng đạt tỷ lệ tiêu diệt (kill rate) tối đa.
- **Arithmetic equation solver**: Đại diện cho logic thuật toán tính toán gần đúng phức tạp. Được chọn để minh họa khoảng cách giữa "Code Coverage cao/Test Pass" và "Khả năng thực sự phát hiện lỗi của Test Suite", vì các biến đổi nhỏ trong thuật toán xấp xỉ rất dễ lọt qua các assertion thông thường.

---

## 2. Kết quả mong đợi khi test

| Chức năng | Kỳ vọng trước khi chạy mutmut |
| :--- | :--- |
| **Basic arithmetic** | Các test case hiện có sẽ tiêu diệt (kill) 100% các đột biến thay đổi toán tử toán học (ví dụ: đổi `+` thành `-`, `*` thành `/`). |
| **Arithmetic equation solver** | Dù Code Coverage đạt rất cao, nhiều đột biến (như thay đổi số lần lặp, cận biên chia đôi, hoặc toán tử so sánh ngưỡng sai số) dự kiến sẽ **Survived**. Lý do là sự thay đổi nhỏ ở biên thuật toán xấp xỉ không làm thay đổi đáng kể kết quả làm tròn cuối cùng của bài test. |

---

## 3. Các bước thực hiện test

### 3.1. Thiết lập baseline & kiểm tra Coverage
Chạy bộ test suite ban đầu bằng `pytest` với cấu hình đo độ bao phủ (coverage) để xác nhận toàn bộ test đều pass và ghi nhận mức coverage làm chuẩn.
``` 
    pytest --cov=src --cov-report=term-missing
``` 
``` 
    Name                         Stmts   Miss  Cover   Missing
    ----------------------------------------------------------
    src/calculator/__init__.py       0      0   100%
    src/calculator/core.py          17      1    94%   24
    ----------------------------------------------------------
    TOTAL                           17      1    94%
``` 

### 3.2. Cấu hình & Dọn dẹp môi trường trước khi mutate
Để `mutmut` không bị ảnh hưởng bởi cache cũ và hoạt động chính xác trên layout `src/`, tiến hành xóa sạch các thư mục cache, tệp dịch `.pyc` và cơ sở dữ liệu coverage cũ trước khi khởi chạy.

``` 
    rm -rf mutants/ .mutmut-cache/ .coverage .pytest_cache/
    find . -type f -name "*.pyc" -delete
    mutmut run
``` 
---

## 4. Phân tích kết quả

### 4.1. Bảng tổng hợp cuối cùng

``` 
    Running mutation testing
    ⠙ 32/32  🎉 25 🫥 0  ⏰ 0  🤔 0  🙁 7  🔇 0  🧙 0
    6.78 mutations/second
``` 

| File | Total Mutants | Killed (🎉) | Survived (🙁) | Code Coverage | Mutation Score |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `src/calculator/core.py` | 32 | **25** | **7** | **94%** | **78.12%** |

### 4.2. Phân tích chi tiết 7 Mutants Sống sót (Survived)

Dưới đây là phân tích nguyên nhân cho 7 đột biến sống sót (trích xuất từ dữ liệu tra cứu lệnh `mutmut browse`):

| # | Vị trí Đột biến (Original -> Mutant) | Phân tích nguyên nhân Sống sót (Reasoning) |
| :---: | :--- | :--- |
| **1** | Hàm `divide(a, b)`:<br>`- if b == 0: raise ValueError("Cannot divide by zero.")`<br>`+ if b == 0: raise ValueError("XXCannot divide by zero.XX")` | Test có assertion kiểm tra việc ném ra ngoại lệ `ValueError`, nhưng **chưa assert nội dung chuỗi thông báo lỗi** (raise ValueError is never directly tested for message string). |
| **2** | Hàm `solve_linear_equation`:<br>`- def solve_linear_equation(func, y, guess=0, ...)`<br>`+ def solve_linear_equation(func, y, guess=1, ...)` | Biến tham số mặc định `guess` **không bao giờ được sử dụng** bên trong thân hàm (variable was never used in the function). Đây là Dead-code/Redundant parameter. |
| **3** | Khởi tạo giới hạn dưới Bisection:<br>`- low, high = -1000, 1000`<br>`+ low, high = -1001, 1000` | Sự thay đổi phạm vi quá nhỏ (1 đơn vị ở biên dưới). Thuật toán chia đôi vẫn hội tụ đúng nghiệm, test case bị bypass. |
| **4** | Khởi tạo giới hạn trên Bisection:<br>`- low, high = -1000, 1000`<br>`+ low, high = -1000, 1001` | Tương tự mutant #3, sự thay đổi vi mô ở biên trên không làm ảnh hưởng đến kết quả tìm nghiệm của các test case hiện tại. |
| **5** | Vòng lặp tối đa Bisection:<br>`- for _ in range(100):`<br>`+ for _ in range(101):` | Tăng giới hạn lặp từ 100 lên 101. Do các phương trình trong test case đều hội tụ và `return` sớm trước 100 lần lặp, đột biến này bị bỏ qua hoàn toàn. |
| **6** | Ngưỡng sai số hội tụ:<br>`- if abs(val) < tolerance:`<br>`+ if abs(val) <= tolerance:` | Thay đổi toán tử `<` thành `<=` tại ngưỡng `1e-7`. Khác biệt cực nhỏ này không làm thay đổi giá trị nghiệm làm tròn trong assertion. |
| **7** | Cập nhật cận chia đôi:<br>`- if val > 0: high = mid`<br>`+ if val >= 0: high = mid` | Thay đổi `>` thành `>=`. Trường hợp `val == 0` chính là lúc nghiệm đã đạt chính xác tuyệt đối, ranh giới này cực kỳ khó kích hoạt với số thực nhị phân trong các test case bình thường. |

---

## 5. So sánh hiệu quả test giữa 2 chức năng & Kết luận

| Tiêu chí | Basic arithmetic (Toán số học) | Arithmetic equation solver (Giải phương trình) |
| :--- | :--- | :--- |
| **Mutation Score** | Gần đạt tối đa (Killed toàn bộ các toán tử số học bị thay đổi). | Bị lọt 7 mutants tại các tham số biên, vòng lặp và ngoại lệ. |
| **Code Coverage** | 100% | 94% (thiếu dòng return fallback cuối cùng ở dòng 24). |
| **Loại lỗ hổng minh họa** | Không đáng kể. | **Thiếu kiểm tra nội dung ngoại lệ** (Mutant #1) và **Dead-code trong tham số hàm** (Mutant #2). |
| **Cách khắc phục** | Duy trì bộ test hiện tại. | - Bổ sung `assert str(exc_info.value) == "Cannot divide by zero."`.<br>- Xóa bỏ hoặc triển khai logic cho tham số `guess` trong `solve_linear_equation`.<br>- Bổ sung test case với hàm hội tụ chậm để kiểm thử ranh giới vòng lặp. |

**Kết luận (Test Effectiveness):**
1. **Coverage cao không đồng nghĩa với Test Suite mạnh:** Báo cáo cho thấy dù `src/calculator/core.py` đạt **94% Code Coverage**, nhưng Mutation Score chỉ đạt **78.12%** (7/32 mutants sống sót).
2. **Khác biệt bản chất thuật toán:** Các hàm số học cơ bản có tính khắt khe cao (đổi dấu là sai kết quả ngay). Ngược lại, các thuật toán tìm nghiệm gần đúng (numerical solvers) có khả năng "chịu lỗi" hoặc che giấu các thay đổi nhỏ tại biên (`range`, bounds, `<` vs `<=`), khiến unit test thông thường rất khó phát hiện.
3. **Giá trị thực tiễn của mutmut:** Công cụ đã chỉ ra chính xác lỗ hổng assertion trong xử lý ngoại lệ và phát hiện tham số thừa (`guess`) không được sử dụng trong code — những lỗi mà công cụ đo Coverage truyền thống hoàn toàn bỏ qua.