# Tổng quan về Mutation Testing

## 1. Mục tiêu

Phần này giải thích ý tưởng cơ bản của Mutation Testing và lý do kỹ thuật này được dùng để đánh giá chất lượng của một bộ kiểm thử. Mutation Testing tập trung vào một câu hỏi chính: nếu source code bị thay đổi nhẹ theo hướng sai, các test hiện tại có phát hiện được thay đổi đó không?

## 2. Câu hỏi chính

- **Mutation Testing là gì?**
- **Mutation Testing giải quyết vấn đề gì?**

Trả lời ngắn gọn:

Mutation Testing là một kỹ thuật software testing dùng để đánh giá Test Effectiveness. Kỹ thuật này tạo ra các thay đổi nhỏ có chủ ý trong source code, gọi là **mutant**. Sau khi mutant được tạo ra, bộ test hiện có được chạy lại; nếu test thất bại, mutant được xem là **killed**, nếu test vẫn pass, mutant được xem là **survived**. Kỹ thuật này giúp phát hiện các test case yếu: một project có thể có Code Coverage cao nhưng test vẫn có chất lượng thấp nếu thiếu assertion mạnh hoặc thiếu các boundary case quan trọng, và Mutation Testing giải quyết vấn đề đó bằng cách kiểm tra xem bộ kiểm thử có phát hiện được các thay đổi logic nhỏ trong code hay không.

## 3. Ghi chú chính

### 3.1 Mục đích của Mutation Testing

Mutation Testing không chủ yếu dùng để tìm bug trong production code. Thay vào đó, nó được dùng để đo độ mạnh của bộ kiểm thử.

Ý tưởng cơ bản:

1. Bắt đầu từ source code gốc.
2. Tạo một thay đổi nhỏ trong code.
3. Chạy các test hiện có.
4. Kiểm tra xem test có phát hiện được thay đổi đó không.

### 3.2 Các thay đổi nhỏ thường gặp

- Đổi `>` thành `>=`.
- Đổi `+` thành `-`.
- Đổi `true` thành `false`.
- Đổi `&&` thành `||`.
- Đổi giá trị return.

Nếu nhiều mutant bị killed, test suite mạnh hơn. Nếu nhiều mutant survived, test suite có thể đang thiếu test case quan trọng hoặc thiếu assertion.

## 4. Ví dụ

Code gốc:

```js
function isAdult(age) {
  return age >= 18;
}
```

Phiên bản mutant:

```js
function isAdult(age) {
  return age > 18;
}
```

Trong mutant này, toán tử `>=` được đổi thành `>`.

Nếu test suite chỉ kiểm tra trường hợp sau:

```js
expect(isAdult(20)).toBe(true);
```

Mutant có thể survived vì cả hai phiên bản đều trả về `true` với `age = 20`.

Nhưng nếu test suite kiểm tra boundary value:

```js
expect(isAdult(18)).toBe(true);
```

Mutant sẽ bị killed vì code gốc `18 >= 18` trả về `true`, còn code mutant `18 > 18` trả về `false`. Điều này cho thấy Mutation Testing có thể phát hiện các boundary test bị thiếu.

## 5. Công cụ hỗ trợ lý thuyết này

Ý tưởng "tạo mutant nhỏ rồi chạy lại test suite để phân loại killed/survived" là nguyên lý lõi mà **mọi công cụ mutation testing** đã khảo sát đều triển khai trực tiếp, dù khác ngôn ngữ/nền tảng:

| Công cụ | Ngôn ngữ | Cách thể hiện nguyên lý này |
|---|---|---|
| StrykerJS | JS/TS | Tạo mutant từ AST, chạy lại Jest/Vitest/Mocha, phân loại killed/survived trong report (xem `tool-survey-strykerjs-jest.md`). |
| Stryker.NET | C#/.NET | `dotnet stryker` tạo mutant, chạy VSTest, xuất mutation report (`tool-survey-strykernet-pit.md`). |
| PIT | Java | Mutate bytecode đã compile, chạy JUnit/TestNG (`tool-survey-strykernet-pit.md`). |
| Mutmut / Cosmic Ray | Python | Mutate AST bằng `parso`, chạy `pytest`/`unittest` (`tool-survey-mutmut-cosmicray.md`). |
| Infection / Major | PHP / Java | Mutate AST hoặc nhúng vào bước biên dịch (`tool-survey-infection-major.md`). |

Ngược lại, **Istanbul/nyc, JaCoCo và Jest Coverage** (khảo sát ở `tool-survey-istanbul-jacoco.md` và `tool-survey-strykerjs-jest.md`) **không** triển khai nguyên lý này — các công cụ đó chỉ đo dòng code có được chạy qua hay không, không tạo mutant và không phân loại killed/survived. Đây chính là ranh giới phân biệt hai nhóm công cụ đã khảo sát trong đề tài.

## 6. Ý chính cần ghi nhớ

- Mutation Testing đo độ mạnh của test suite, không phải đi tìm bug trực tiếp trong production code.
- Mutant được tạo bằng cách thay đổi nhỏ, có chủ ý trong source code.
- `Killed` nghĩa là test phát hiện được thay đổi; `survived` nghĩa là test không phát hiện được.
- Boundary test (ví dụ `age = 18`) thường là yếu tố quyết định một mutant bị killed hay survived.
- Mọi công cụ mutation testing (StrykerJS, Stryker.NET, PIT, Mutmut, Cosmic Ray, Infection, Major) đều triển khai đúng nguyên lý này; các công cụ đo coverage thuần tuý (Istanbul/nyc, JaCoCo, Jest Coverage) thì không.

## 7. Tài liệu tham khảo

- https://stryker-mutator.io/docs/
- https://testrigor.com/blog/understanding-mutation-testing-a-comprehensive-guide/
