# Khảo sát công cụ: StrykerJS và Jest Coverage

## 1. Mục tiêu

Mục tiêu của phần này là tìm hiểu hai công cụ liên quan đến việc đánh giá chất lượng test suite trong dự án JavaScript/TypeScript:

- **StrykerJS**: công cụ mutation testing dùng để đánh giá test suite có phát hiện được lỗi logic hay không.
- **Jest Coverage**: tính năng đo code coverage trong Jest, dùng để biết phần code nào đã được test chạy qua.

Hai công cụ này giúp nhóm làm rõ sự khác nhau giữa **code coverage** và **mutation testing** trong chủ đề **Mutation Testing & Test Effectiveness**.

## 2. StrykerJS

### 2.1 Tổng quan công cụ

StrykerJS là công cụ mutation testing cho hệ sinh thái JavaScript/TypeScript. Nó tạo ra các thay đổi nhỏ trong source code, gọi là **mutants**, sau đó chạy lại test suite để kiểm tra xem test có phát hiện được các thay đổi sai đó hay không.

Theo tài liệu Stryker, StrykerJS hỗ trợ nhiều loại dự án JavaScript hiện đại như TypeScript, React, Angular, Vue, Svelte và Node.js.

### 2.2 Mục đích chính

Mục đích chính của StrykerJS là đánh giá **test effectiveness**, tức là mức độ hiệu quả của test suite.

StrykerJS không chỉ kiểm tra dòng code nào được chạy qua, mà kiểm tra sâu hơn:

- Test có phát hiện được lỗi logic không?
- Assertion có đủ mạnh không?
- Có thiếu boundary test không?
- Có test nào chỉ tăng coverage nhưng không kiểm tra kết quả thật không?

Nếu một mutant bị test phát hiện, mutant đó được xem là **killed**. Nếu test vẫn pass, mutant đó **survived**.

### 2.3 Ngôn ngữ/Nền tảng hỗ trợ

StrykerJS hỗ trợ chủ yếu:

- JavaScript
- TypeScript
- Node.js
- React
- Angular
- Vue
- Svelte

Ngoài ra, StrykerJS có thể tích hợp với nhiều test runner phổ biến như Jest, Mocha, Jasmine, Karma, Vitest và các môi trường kiểm thử JavaScript khác.

### 2.4 Cách công cụ hoạt động

Quy trình hoạt động cơ bản của StrykerJS:

1. Chạy test suite trên code gốc để đảm bảo test ban đầu pass.
2. Phân tích source code và tạo ra các mutant.
3. Mỗi mutant là một thay đổi nhỏ trong code, ví dụ đổi `>=` thành `>`.
4. Chạy lại test suite với từng mutant.
5. Nếu test fail, mutant bị **killed**.
6. Nếu test vẫn pass, mutant **survived**.
7. Sinh report thể hiện mutation score và danh sách mutant.

Ví dụ:

```js
function isAdult(age) {
  return age >= 18;
}
```

StrykerJS có thể tạo mutant:

```js
function isAdult(age) {
  return age > 18;
}
```

Nếu test không kiểm tra `age = 18`, mutant này có thể sống sót. Điều đó cho thấy test suite còn thiếu boundary case.

### 2.5 Tính năng chính

Các tính năng chính của StrykerJS:

- Tạo mutant tự động từ source code.
- Chạy test suite trên từng mutant.
- Tính mutation score.
- Phân loại mutant: killed, survived, timeout, no coverage.
- Hỗ trợ nhiều test runner trong JavaScript ecosystem.
- Có nhiều dạng report, ví dụ text report, HTML report, dashboard.
- Hỗ trợ cấu hình file, phạm vi mutate, reporter và plugin.
- Có thể dùng để phát hiện test yếu, thiếu assertion hoặc thiếu boundary case.

### 2.6 Trường hợp sử dụng phổ biến

StrykerJS thường được dùng trong các trường hợp:

- Đánh giá chất lượng unit test.
- Kiểm tra test suite của các hàm business logic quan trọng.
- So sánh chất lượng test trước và sau khi bổ sung test case.
- Tìm các đoạn code có coverage cao nhưng test vẫn yếu.

### 2.7 Điểm mạnh

Điểm mạnh của StrykerJS:

- Đánh giá test suite sâu hơn code coverage.
- Phù hợp với JavaScript/TypeScript, dễ liên hệ với các project web hiện nay.
- Có report rõ ràng, dễ dùng cho demo.
- Hỗ trợ nhiều framework và test runner.
- Giúp phát hiện các test case yếu hoặc thiếu assertion.
- Có thể demo trực quan bằng cách cho mutant sống trước, sau đó thêm test để kill mutant.

### 2.8 Giới hạn

Một số giới hạn của StrykerJS:

- Chạy chậm hơn test thông thường vì phải chạy test nhiều lần trên nhiều mutant.
- Cần test suite ban đầu ổn định.
- Có thể sinh ra equivalent mutants, tức là mutant có thay đổi code nhưng hành vi không đổi.
- Với project lớn, cần giới hạn phạm vi mutate để tránh thời gian chạy quá lâu.
- Người dùng cần hiểu report để phân biệt mutant sống do test yếu hay do equivalent mutant.

### 2.9 Chi phí/Giấy phép

Stryker là công cụ open-source và được phát hành dưới giấy phép **Apache 2.0**.

Vì vậy, nhóm có thể sử dụng miễn phí cho học tập, nghiên cứu và demo seminar.

### 2.10 Hỗ trợ AI, nếu có

StrykerJS không phải là công cụ AI và tài liệu chính thức không thể hiện tính năng AI tích hợp sẵn.

Tuy nhiên, AI có thể hỗ trợ khi dùng StrykerJS ở các bước:

- Giải thích mutation report.
- Gợi ý test case để kill survived mutants.
- Phân tích vì sao mutant survived.
- Viết thêm boundary test hoặc negative test.

### 2.11 Tiềm năng demo

StrykerJS có tiềm năng demo rất cao.

Lý do:

- Dễ tạo ví dụ nhỏ bằng JavaScript.
- Dễ tạo mutant liên quan đến toán tử so sánh như `>=` thành `>`.
- Có thể minh họa rõ ràng khái niệm killed mutant và survived mutant.
- Có thể kết hợp với Jest để cho thấy coverage cao chưa chắc test mạnh.
- Phù hợp với chủ đề Mutation Testing & Test Effectiveness.

Kịch bản demo đề xuất:

1. Tạo một hàm đơn giản như `isAdult(age)`.
2. Viết test chưa đủ mạnh.
3. Chạy StrykerJS và cho thấy có survived mutant.
4. Bổ sung boundary test.
5. Chạy lại và cho thấy mutant bị killed.

### 2.12 Tài liệu tham khảo

- https://stryker-mutator.io/docs/
- https://stryker-mutator.io/docs/stryker-js/introduction/

## 3. Jest Coverage

### 3.1 Tổng quan công cụ

Jest Coverage không phải là một công cụ mutation testing riêng biệt. Đây là tính năng đo code coverage được tích hợp trong Jest.

Jest là testing framework phổ biến cho JavaScript. Khi bật coverage, Jest sẽ thu thập thông tin về phần code nào đã được test chạy qua và xuất báo cáo coverage.

Jest Coverage thường được dùng để đo:

- Line coverage
- Branch coverage
- Function coverage
- Statement coverage

### 3.2 Mục đích chính

Mục đích chính của Jest Coverage là cho biết test suite đã chạy qua bao nhiêu phần trăm code.

Nó giúp nhóm trả lời các câu hỏi:

- Dòng code nào đã được test chạy qua?
- Function nào đã được gọi trong test?
- Branch nào chưa được test?
- File nào có coverage thấp?

Tuy nhiên, Jest Coverage không cho biết test có assertion tốt hay không. Vì vậy, nó đo được **mức độ code được chạy qua**, nhưng không đo đầy đủ **khả năng phát hiện lỗi logic**.

### 3.3 Ngôn ngữ/Nền tảng hỗ trợ

Jest Coverage hỗ trợ chủ yếu:

- JavaScript
- TypeScript
- Node.js
- React
- Một số framework frontend/backend JavaScript khác

Jest có thể dùng với TypeScript thông qua Babel hoặc `ts-jest`. Khi dùng Babel, TypeScript được transpile, nhưng Jest không tự type-check trong quá trình chạy test.

### 3.4 Cách công cụ hoạt động

Khi bật coverage, Jest sẽ instrument code để thu thập dữ liệu trong lúc chạy test.

Có thể chạy coverage bằng CLI:

```bash
jest --coverage
```

Hoặc cấu hình trong `jest.config.js`:

```js
module.exports = {
  collectCoverage: true,
};
```

Sau khi chạy test, Jest sẽ sinh coverage report, thường nằm trong thư mục:

```text
coverage/
```

Report có thể cho biết:

- Bao nhiêu phần trăm statements được chạy.
- Bao nhiêu phần trăm branches được chạy.
- Bao nhiêu functions được gọi.
- Bao nhiêu lines được chạy.

Jest hỗ trợ coverage provider là `babel` hoặc `v8`.

### 3.5 Tính năng chính

Các tính năng chính của Jest Coverage:

- Bật coverage bằng `--coverage` hoặc `collectCoverage`.
- Hỗ trợ `collectCoverageFrom` để chọn file cần đo coverage.
- Hỗ trợ `coverageDirectory` để cấu hình thư mục output.
- Hỗ trợ `coverageReporters` như text, lcov, json, clover.
- Hỗ trợ `coverageThreshold` để đặt ngưỡng coverage tối thiểu.
- Có thể fail test nếu coverage thấp hơn ngưỡng yêu cầu.
- Có thể dùng trong CI/CD để đảm bảo coverage không giảm.

Ví dụ cấu hình threshold:

```js
module.exports = {
  collectCoverage: true,
  coverageThreshold: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80,
    },
  },
};
```

### 3.6 Trường hợp sử dụng phổ biến

Jest Coverage thường được dùng để:

- Kiểm tra mức độ bao phủ của test suite.
- Phát hiện file hoặc branch chưa được test.
- Theo dõi coverage trong quá trình phát triển.
- Đặt coverage threshold trong CI/CD.
- Làm bước kiểm tra cơ bản trước khi dùng mutation testing.

Trong seminar, Jest Coverage phù hợp để chứng minh rằng code coverage cao không đồng nghĩa với test suite mạnh.

### 3.7 Điểm mạnh

Điểm mạnh của Jest Coverage:

- Dễ bật và dễ chạy.
- Tích hợp trực tiếp trong Jest.
- Report dễ đọc.
- Phù hợp với JavaScript/TypeScript project.
- Có thể dùng nhanh trong demo.
- Giúp phát hiện phần code chưa được test chạy qua.
- Có thể kết hợp với coverage threshold để kiểm soát chất lượng cơ bản.

### 3.8 Giới hạn

Giới hạn lớn nhất của Jest Coverage là nó chỉ đo việc code có được chạy qua hay không.

Nó không kiểm tra:

- Assertion có đúng và đủ mạnh không.
- Test có phát hiện được lỗi logic không.
- Boundary case có được kiểm tra không.
- Expected result có thực sự được verify không.

Ví dụ một test như sau vẫn có thể tăng coverage:

```js
test("calls isAdult", () => {
  isAdult(20);
});
```

Nhưng test này không có assertion, nên gần như không kiểm tra hành vi đúng sai.

Vì vậy, coverage cao chỉ cho biết test đã chạy qua code, không đảm bảo test có chất lượng cao.

### 3.9 Chi phí/Giấy phép

Jest là công cụ open-source và được phát hành dưới giấy phép **MIT**.

Do đó, Jest Coverage có thể được sử dụng miễn phí trong học tập, nghiên cứu và dự án thực tế.

### 3.10 Hỗ trợ AI, nếu có

Jest Coverage không có tính năng AI tích hợp trực tiếp trong phần coverage.

Tuy nhiên, AI có thể hỗ trợ khi dùng Jest Coverage:

- Đọc coverage report.
- Gợi ý test case cho file có coverage thấp.
- Gợi ý branch hoặc edge case cần test.
- Viết thêm unit test dựa trên uncovered lines.

### 3.11 Tiềm năng demo

Jest Coverage có tiềm năng demo cao, đặc biệt khi dùng để so sánh với StrykerJS.

Kịch bản demo đề xuất:

1. Viết một hàm JavaScript đơn giản.
2. Viết test làm coverage đạt cao.
3. Cho thấy coverage report có thể tốt.
4. Nhưng test vẫn thiếu boundary case hoặc assertion mạnh.
5. Chạy StrykerJS để cho thấy mutant vẫn survived.
6. Kết luận: coverage là cần thiết nhưng chưa đủ để đánh giá test effectiveness.

### 3.12 Tài liệu tham khảo

- https://jestjs.io/docs/getting-started
- https://jestjs.io/docs/configuration
- https://jestjs.io/docs/cli
- https://raw.githubusercontent.com/jestjs/jest/main/LICENSE

## 4. Ghi chú tổng kết

StrykerJS và Jest Coverage đều liên quan đến đánh giá chất lượng test, nhưng chúng đo hai khía cạnh khác nhau.

- **Jest Coverage** cho biết test đã chạy qua phần nào của code.
- **StrykerJS** cho biết test có phát hiện được lỗi logic khi code bị thay đổi hay không.

Vì vậy, Jest Coverage phù hợp để kiểm tra mức độ bao phủ cơ bản, còn StrykerJS phù hợp để đánh giá sâu hơn về test effectiveness.

Trong seminar, hai công cụ này có thể kết hợp rất tốt:

1. Dùng Jest Coverage để cho thấy coverage có thể cao.
2. Dùng StrykerJS để cho thấy test vẫn có thể yếu.
3. Bổ sung test case tốt hơn.
4. Chạy lại mutation testing để chứng minh test suite đã được cải thiện.
