# Tổng quan về Mutation Testing

## 1. Mục tiêu

Phần này giải thích ý tưởng cơ bản của Mutation Testing và lý do kỹ thuật này được dùng để đánh giá chất lượng của một test suite.

Mutation Testing tập trung vào một câu hỏi chính:

> Nếu source code bị thay đổi nhẹ theo hướng sai, các test hiện tại có phát hiện được thay đổi đó không?

## 2. Câu hỏi chính

### Mutation Testing là gì?

Mutation Testing là một kỹ thuật software testing dùng để đánh giá Test Effectiveness. Kỹ thuật này tạo ra các thay đổi nhỏ có chủ ý trong source code. Mỗi phiên bản code đã bị thay đổi được gọi là một **mutant**.

Sau khi các mutant được tạo ra, test suite sẽ được chạy lại. Nếu test thất bại, mutant đó được xem là **killed**. Nếu test vẫn pass, mutant đó được xem là **survived**.

### Mutation Testing giải quyết vấn đề gì?

Mutation Testing giúp phát hiện các test case yếu. Một project có thể có Code Coverage cao, nhưng test vẫn có chất lượng thấp nếu thiếu assertion mạnh hoặc thiếu các boundary case quan trọng.

Mutation Testing giải quyết vấn đề này bằng cách kiểm tra xem test suite có phát hiện được các thay đổi logic nhỏ trong code hay không.

## 3. Ghi chú chính

Mutation Testing không chủ yếu dùng để tìm bug trong production code. Thay vào đó, nó được dùng để đo độ mạnh của test suite.

Ý tưởng cơ bản:

1. Bắt đầu từ source code gốc.
2. Tạo một thay đổi nhỏ trong code.
3. Chạy các test hiện có.
4. Kiểm tra xem test có phát hiện được thay đổi đó không.

Một số thay đổi nhỏ thường gặp:

- Đổi `>` thành `>=`
- Đổi `+` thành `-`
- Đổi `true` thành `false`
- Đổi `&&` thành `||`
- Đổi giá trị return

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

Mutant sẽ bị killed vì:

- Code gốc: `18 >= 18` trả về `true`
- Code mutant: `18 > 18` trả về `false`

Điều này cho thấy Mutation Testing có thể phát hiện các boundary test bị thiếu.

## 5. Ý chính cần ghi nhớ

- Mutation Testing đánh giá chất lượng của test case.
- Mutant là một phiên bản code được thay đổi nhỏ từ code gốc.
- Mutant bị killed nghĩa là test suite phát hiện được thay đổi.
- Mutant survived nghĩa là test suite không phát hiện được thay đổi.
- Mutation Testing hữu ích vì Code Coverage cao không luôn đồng nghĩa với test mạnh.
- Kỹ thuật này giúp tester tìm assertion bị thiếu, boundary case bị thiếu và logic test yếu.

## 6. Tài liệu tham khảo

- https://stryker-mutator.io/docs/
- https://stryker-mutator.io/docs/mutation-testing-elements/supported-mutators/
- https://testrigor.com/blog/understanding-mutation-testing-a-comprehensive-guide/

