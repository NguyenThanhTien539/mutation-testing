# Khảo sát công cụ: Stryker.NET và PIT

## 1. Mục tiêu

Nghiên cứu bối cảnh, mục đích và cách sử dụng Stryker.NET và PIT cho seminar **Mutation Testing & Test Effectiveness**.

Hai công cụ này cùng phục vụ một mục tiêu: đánh giá chất lượng của `test suite` bằng cách tạo các phiên bản code bị thay đổi nhỏ gọi là `mutants`, sau đó chạy test hiện có để xem test có phát hiện được lỗi được chèn vào hay không. Nếu test fail, mutant bị `killed`; nếu test vẫn pass, mutant `survived`. Kết quả cuối cùng giúp nhóm đánh giá mức độ hiệu quả của test suite tốt hơn so với chỉ nhìn vào line coverage.

Stryker.NET đại diện cho mutation testing trong hệ sinh thái .NET/C#, còn PIT đại diện cho mutation testing trong hệ sinh thái Java/JVM. Việc khảo sát cả hai giúp nhóm so sánh cách cùng một kỹ thuật testing được triển khai khác nhau tùy platform.

## 2. Stryker.NET

### 2.1 Tổng quan công cụ

Stryker.NET là công cụ mutation testing dành cho .NET. Đây là một thành viên trong hệ sinh thái Stryker Mutator, tập trung vào việc kiểm tra chất lượng test cho các project C#/.NET.

Stryker.NET hoạt động bằng cách tạo ra các `mutants` từ source code C#, sau đó chạy test suite trên từng mutant. Nếu test suite phát hiện được thay đổi sai và fail, mutant bị `killed`. Nếu toàn bộ test vẫn pass, mutant `survived`, cho thấy có thể đang thiếu test case hoặc assertion.

### 2.2 Mục đích chính

Mục đích chính của Stryker.NET là **test your tests**, nghĩa là kiểm tra xem test suite hiện tại có thật sự bắt được lỗi hay chỉ đơn giản là chạy qua code.

Stryker.NET giúp trả lời các câu hỏi:

- Test suite có bắt được lỗi logic không?
- Code coverage cao có thật sự đi kèm assertion tốt không?
- Có branch, condition hoặc business rule nào được execute nhưng chưa được kiểm tra đúng behavior không?
- Mutation score của project có đủ tốt để tin tưởng test suite không?

### 2.3 Ngôn ngữ/Nền tảng hỗ trợ

Stryker.NET hỗ trợ hệ sinh thái .NET, chủ yếu là:

- C#.
- .NET Core.
- .NET Framework.
- Project dùng `.csproj` hoặc `.sln`.
- Test runner trong .NET như VSTest và Microsoft Testing Platform.

Stryker.NET được cài và chạy thông qua .NET CLI:

```bash
dotnet tool install -g dotnet-stryker
dotnet stryker
```

### 2.4 Cách công cụ hoạt động

Quy trình hoạt động cơ bản:

1. Stryker.NET đọc project và xác định source files cần mutate.
2. Tool tạo mutants bằng các `mutation operators`.
3. Tool chạy test suite trên từng mutant.
4. Nếu có test fail, mutant được đánh dấu là `killed`.
5. Nếu test pass hết, mutant được đánh dấu là `survived`.
6. Tool tạo mutation report, mutation score và danh sách mutants cần review.

Ví dụ mutation:

```csharp
// Original code
return age >= 18;

// Mutant
return age > 18;
```

Nếu test suite không có case `age = 18`, mutant này có thể `survived`.

### 2.5 Tính năng chính

| Tính năng             | Mô tả                                                                                     |
| --------------------- | ----------------------------------------------------------------------------------------- |
| Mutation levels       | Hỗ trợ các level như Basic, Standard, Advanced, Complete.                                 |
| Mutators              | Hỗ trợ arithmetic, logical, equality, boolean, string, regex, LINQ, method/block removal. |
| Reporters             | Có HTML, progress, cleartext, cleartexttree, dots, JSON, Markdown, dashboard.             |
| Thresholds            | Có `high`, `low`, `break` để đánh giá hoặc fail CI khi score thấp.                        |
| Coverage analysis     | Có `perTest`, `perTestInIsolation`, `all`, `off` để tối ưu runtime.                       |
| Changed-code workflow | Có `since` và `with-baseline` để chạy mutation testing trên phần code thay đổi.           |
| Test runner support   | Mặc định dùng VSTest, có Microsoft Testing Platform ở trạng thái preview.                 |

Ví dụ cấu hình threshold:

```json
{
  "stryker-config": {
    "thresholds": {
      "high": 80,
      "low": 60,
      "break": 50
    }
  }
}
```

### 2.6 Trường hợp sử dụng phổ biến

Stryker.NET phù hợp trong các trường hợp:

- Kiểm tra chất lượng unit tests trong C#/.NET project.
- Phát hiện test chỉ có coverage nhưng thiếu assertion.
- Tìm missing boundary tests, ví dụ `>=` thành `>`.
- Đánh giá test suite cho business logic quan trọng.
- Tích hợp vào CI/CD với mutation score threshold.
- Chạy targeted mutation testing trên changed code trước pull request.
- Demo mutation testing cho seminar với project C# nhỏ.

### 2.7 Điểm mạnh

- Native với .NET/C# ecosystem.
- Chạy đơn giản bằng `dotnet stryker`.
- Report trực quan, đặc biệt là HTML report.
- Có nhiều reporter phù hợp cả local development và CI.
- Có mutation levels giúp điều chỉnh độ nghiêm ngặt.
- Có thresholds để dùng như quality gate.
- Có `since` và baseline giúp giảm thời gian chạy trên project lớn.
- Dễ trình bày trong demo vì mutation result gắn trực tiếp với source code C#.

### 2.8 Giới hạn

- Mutation testing có thể chạy lâu với solution lớn.
- Cấu hình nhiều test projects có thể phức tạp.
- Một số behavior đặc thù của xUnit/NUnit theories hoặc parameterized tests có thể ảnh hưởng coverage capture và test identification.
- Microsoft Testing Platform runner vẫn ở preview nên cần verify kết quả.
- Một số `survived mutants` có thể là `equivalent mutants`, cần review thủ công.
- Không phù hợp để chạy full mutation suite ở mọi commit nếu project lớn.

### 2.9 Chi phí/Giấy phép

Stryker.NET là công cụ open-source và miễn phí sử dụng.

Stryker Dashboard có thể được dùng thêm nếu team muốn quản lý hoặc hiển thị report tập trung, nhưng bản thân Stryker.NET có thể chạy local và tạo report mà không cần trả phí.

### 2.10 Hỗ trợ AI, nếu có

Stryker.NET không phải AI tool. Tuy nhiên, kết quả của Stryker.NET có thể kết hợp tốt với AI trong các tác vụ:

- Phân tích `survived mutants`.
- Gợi ý missing assertions.
- Đề xuất thêm boundary test cases.
- Summarize mutation report.
- Giải thích vì sao một mutant survived.
- Tạo test case mới dựa trên mutation operator.

Ví dụ: nếu report cho thấy mutant `age >= 18` thành `age > 18` survived, AI có thể gợi ý thêm test tại boundary `age = 18`.

### 2.11 Tài liệu tham khảo

- [Stryker.NET introduction](https://stryker-mutator.io/docs/stryker-net/introduction/)
- [Stryker.NET getting started](https://stryker-mutator.io/docs/stryker-net/getting-started/)
- [Stryker.NET configuration](https://stryker-mutator.io/docs/stryker-net/configuration/)
- [Stryker.NET mutations](https://stryker-mutator.io/docs/stryker-net/mutations/)
- [Stryker.NET reporters](https://stryker-mutator.io/docs/stryker-net/reporters/)
- [Stryker mutant states and metrics](https://stryker-mutator.io/docs/mutation-testing-elements/mutant-states-and-metrics/)

## 3. PIT

### 3.1 Tổng quan công cụ

PIT, thường gọi là Pitest, là công cụ mutation testing phổ biến cho Java/JVM project. PIT được thiết kế để kiểm tra chất lượng unit tests trong Java bằng cách tạo mutants từ compiled bytecode rồi chạy test suite để đánh giá test có phát hiện được lỗi không.

Khác với cách nhiều người hình dung là sửa source code trực tiếp, PIT mutate Java bytecode. Điều này giúp PIT chạy nhanh hơn và dễ tích hợp vào build tool như Maven.

### 3.2 Mục đích chính

Mục đích chính của PIT là đánh giá test effectiveness trong Java project.

PIT giúp trả lời:

- Unit tests có phát hiện được lỗi được chèn vào không?
- Những dòng code nào có coverage nhưng assertion yếu?
- Có logic nào bị thay đổi mà test vẫn pass không?
- Mutation score của Java project có đủ tốt không?
- Test suite có cần thêm boundary, negative hoặc behavior-based tests không?

### 3.3 Ngôn ngữ/Nền tảng hỗ trợ

PIT hỗ trợ:

- Java.
- JVM projects.
- Maven.
- Ant.
- Command line.
- Gradle thông qua third-party plugin.
- JUnit và TestNG.

Theo PIT FAQ, JUnit 5 không được hỗ trợ out of the box và cần plugin riêng.

Ví dụ Maven setup:

```xml
<plugin>
  <groupId>org.pitest</groupId>
  <artifactId>pitest-maven</artifactId>
  <version>LATEST</version>
</plugin>
```

Chạy PIT bằng Maven:

```bash
mvn test-compile org.pitest:pitest-maven:mutationCoverage
```

### 3.4 Cách công cụ hoạt động

Quy trình hoạt động cơ bản:

1. PIT compile hoặc dùng compiled classes của Java project.
2. PIT tạo mutants ở bytecode level.
3. PIT chạy line coverage analysis để biết test nào cover dòng code nào.
4. PIT dùng coverage data và test timing để chọn test liên quan cho từng mutant.
5. PIT chạy tests trên từng mutant.
6. PIT phân loại kết quả: `killed`, `survived`, `no coverage`, `timed out`, `non viable`, `memory error`, hoặc `run error`.
7. PIT tạo HTML/XML/CSV report.

Ví dụ mutation:

```java
// Original logic
if (i >= 0) {
    return "foo";
}

// Mutant
if (i > 0) {
    return "foo";
}
```

Nếu test không kiểm tra boundary `i = 0`, mutant này có thể `survived`.

### 3.5 Tính năng chính

| Tính năng                 | Mô tả                                                                                          |
| ------------------------- | ---------------------------------------------------------------------------------------------- |
| Bytecode mutation         | Mutate compiled bytecode thay vì source code.                                                  |
| Maven integration         | Tích hợp mạnh với Maven qua `pitest-maven`.                                                    |
| Mutator groups            | Có các nhóm như `DEFAULTS`, `STRONGER`, `ALL`.                                                 |
| Built-in mutators         | Có conditionals boundary, increments, math, negate conditionals, returns, method call removal. |
| Coverage-guided execution | Dùng line coverage để chọn tests liên quan đến mutant.                                         |
| Test prioritization       | Dùng test timing và naming convention để ưu tiên tests.                                        |
| Reports                   | Hỗ trợ HTML, XML, CSV.                                                                         |
| Thresholds                | Có `mutationThreshold`, `coverageThreshold`, `testStrengthThreshold`.                          |
| Incremental analysis      | Có experimental incremental analysis cho codebase lớn.                                         |

Một số mutators phổ biến:

| Mutator                 | Ví dụ                           |
| ----------------------- | ------------------------------- |
| `CONDITIONALS_BOUNDARY` | `<` thành `<=`, `>=` thành `>`  |
| `INCREMENTS`            | `i++` thành `i--`               |
| `MATH`                  | Thay đổi arithmetic operations  |
| `NEGATE_CONDITIONALS`   | `==` thành `!=`, `<=` thành `>` |
| `VOID_METHOD_CALLS`     | Remove calls tới void methods   |
| `FALSE_RETURNS`         | Boolean return thành `false`    |
| `TRUE_RETURNS`          | Boolean return thành `true`     |
| `NULL_RETURNS`          | Object return thành `null`      |
| `PRIMITIVE_RETURNS`     | Primitive return thành `0`      |

### 3.6 Trường hợp sử dụng phổ biến

PIT phù hợp trong các trường hợp:

- Java project dùng Maven.
- Kiểm tra chất lượng unit tests.
- Phát hiện missing boundary tests.
- Phát hiện tests có line coverage nhưng thiếu assertion.
- Đánh giá test suite cho business logic quan trọng.
- Chạy mutation testing trên changed code hoặc scheduled build.
- Tạo demo cho seminar với Java function và JUnit tests.

### 3.7 Điểm mạnh

- Mature và phổ biến trong Java/JVM ecosystem.
- Tích hợp Maven tốt.
- Bytecode mutation giúp chạy nhanh và phù hợp với build pipeline.
- Có coverage-guided test selection.
- Có report kết hợp line coverage và mutation coverage.
- Có thresholds để fail build nếu score thấp.
- Có incremental analysis cho codebase lớn.
- Mutator system rõ ràng và nhiều ví dụ dễ dùng cho demo.

### 3.8 Giới hạn

- Bytecode mutation khó giải thích hơn source-level mutation.
- Report map bytecode-level mutation về source line, đôi khi không trực quan.
- JUnit 5 cần plugin, không hỗ trợ trực tiếp out of the box.
- Static initializers và enum-related code có thể khó mutate vì chỉ chạy một lần mỗi JVM.
- Integration-heavy tests có thể làm runtime dài.
- Có thể xuất hiện `equivalent mutants` cần review thủ công.

### 3.9 Chi phí/Giấy phép

PIT là công cụ open-source và miễn phí.

PIT có hệ sinh thái mở rộng như Arcmutate cho các nhu cầu nâng cao, ví dụ PR integration, Kotlin, Spring hoặc Git-related workflows. Các phần nâng cao này có thể thuộc dạng commercial/pro, nhưng PIT core vẫn có thể dùng miễn phí.

### 3.10 Hỗ trợ AI, nếu có

PIT không phải AI tool. Tuy nhiên, AI có thể hỗ trợ rất tốt khi đọc và xử lý PIT report:

- Tóm tắt HTML/XML/CSV mutation report.
- Phân loại `survived mutants` theo nguyên nhân.
- Gợi ý JUnit test cases để kill mutants.
- Giải thích bytecode-level mutation bằng source-level terms.
- Đề xuất boundary tests hoặc negative tests.

Ví dụ: nếu PIT cho thấy mutant `>=` thành `>` survived, AI có thể gợi ý thêm test tại đúng boundary value.

### 3.11 Tài liệu tham khảo

- [PIT official site](https://pitest.org/)
- [PIT quickstart](https://pitest.org/quickstart/)
- [PIT Maven quickstart](https://pitest.org/quickstart/maven/)
- [PIT basic concepts](https://pitest.org/quickstart/basic_concepts/)
- [PIT mutation operators](https://pitest.org/quickstart/mutators/)
- [PIT incremental analysis](https://pitest.org/quickstart/incremental_analysis/)
- [PIT FAQ](https://pitest.org/faq/)
