# Setup StrykerJS trên eshop-sut (frontend-web)

## 1. Mục tiêu

Setup StrykerJS để chạy mutation testing trên phân hệ **frontend-web** (React + Vite) của
SUT [`eshop-sut`](https://github.com/KidCute1412/eshop-sut), đã clone vào `demo/eshop-sut/`.

Đây là kết quả **đã chạy thật**, không phải hướng dẫn lý thuyết — mọi lệnh, output và
mutation score trong tài liệu này lấy trực tiếp từ lần chạy thực tế.

## 4. Các bước thực hiện

### Bước 1 — Cài Vitest + Testing Library

Chọn **Vitest** thay vì Jest vì `frontend-web` đã dùng Vite sẵn — Vitest tái dùng luôn cấu
hình Vite, không cần setup transform/babel riêng như Jest.

```bash
cd demo/eshop-sut/frontend-web
npm install -D vitest@4.1.10 jsdom@29.1.1 \
  @testing-library/react@16.3.2 @testing-library/jest-dom@6.9.1 \
  @stryker-mutator/core@9.6.1 @stryker-mutator/vitest-runner@9.6.1
```

### Bước 2 — Bật test environment trong `vite.config.js`

```js
// vite.config.js
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  test: {
    environment: 'jsdom',
    globals: true,
    setupFiles: './test/setupTests.js',
  },
})
```

### Bước 3 — Tạo `test/setupTests.js`

> Cập nhật: toàn bộ file test và setup file ban đầu được viết colocated trong `src/` (ví dụ
> `src/context/CartContext.test.jsx`), sau đó đã dời sang thư mục `test/` riêng (mirror lại
> cấu trúc `src/`) để dễ kiểm soát — xem Bước 11. Nội dung dưới đây đã cập nhật theo đường dẫn
> mới `test/`.

```js
import '@testing-library/jest-dom/vitest';
```

### Bước 4 — Thêm script `test` vào `package.json`

```json
"scripts": {
  "dev": "vite",
  "build": "vite build",
  "lint": "eslint .",
  "preview": "vite preview",
  "test": "vitest run"
}
```

### Bước 5 — Viết test tối thiểu cho `src/context/CartContext.jsx`

Chọn `CartContext.jsx` làm module demo vì đây là logic nghiệp vụ thuần (giỏ hàng), không
phụ thuộc API/localStorage như `AuthContext.jsx`, dễ test và dễ minh hoạ mutation testing.

File `test/context/CartContext.test.jsx`:

```jsx
import { describe, it, expect } from 'vitest';
import { renderHook, act } from '@testing-library/react';
import { CartProvider, useCart } from '../../src/context/CartContext';

const wrapper = ({ children }) => <CartProvider>{children}</CartProvider>;

describe('CartContext', () => {
  it('starts with an empty cart', () => {
    const { result } = renderHook(() => useCart(), { wrapper });
    expect(result.current.cart).toEqual([]);
    expect(result.current.cartTotal).toBe(0);
  });

  it('adds a product to the cart and updates the total', () => {
    const { result } = renderHook(() => useCart(), { wrapper });
    act(() => {
      result.current.addToCart({ id: 1, name: 'Shirt', price: 100000 }, 2);
    });
    expect(result.current.cart).toHaveLength(1);
    expect(result.current.cartTotal).toBe(200000);
  });

  it('clears the cart', () => {
    const { result } = renderHook(() => useCart(), { wrapper });
    act(() => {
      result.current.addToCart({ id: 1, name: 'Shirt', price: 100000 }, 1);
      result.current.clearCart();
    });
    expect(result.current.cart).toEqual([]);
    expect(result.current.cartTotal).toBe(0);
  });
});
```

Lưu ý: bộ test này **cố tình không test `removeFromCart`** — để minh hoạ một phần code
hoàn toàn không có coverage, xem mục 6.

### Bước 6 — Chạy baseline test suite (bắt buộc trước khi chạy Stryker)

```bash
npm test
```

Output thực tế:

```
 RUN  v4.1.10 .../demo/eshop-sut/frontend-web

 Test Files  1 passed (1)
      Tests  3 passed (3)
```

Test suite phải pass sạch trước khi chạy Stryker — Stryker cần baseline ổn định để so sánh.

### Bước 7 — Tạo `stryker.conf.json`

```json
{
  "$schema": "./node_modules/@stryker-mutator/core/schema/stryker-schema.json",
  "packageManager": "npm",
  "testRunner": "vitest",
  "reporters": ["html", "clear-text", "progress"],
  "coverageAnalysis": "perTest",
  "mutate": ["src/context/CartContext.jsx"]
}
```

Giải thích:
- `mutate`: giới hạn phạm vi mutate chỉ 1 file để chạy nhanh (project lớn nên luôn giới hạn
  phạm vi, đây là điểm yếu đã ghi nhận ở `tool-survey/tool-survey-strykerjs-jest.md`).
- `coverageAnalysis: perTest`: Stryker dùng coverage để biết mutant nào được test nào chạy
  qua, giúp chạy nhanh hơn (chỉ chạy các test có liên quan tới mutant đó).
- `reporters: html`: sinh report HTML tại `reports/mutation/mutation.html`.

### Bước 8 — Chạy Stryker

```bash
npx stryker run
```

**Cảnh báo/lưu ý (đã gặp thực tế):** nếu chạy lệnh này **không đứng đúng trong thư mục
`frontend-web`** (nơi đã cài `@stryker-mutator/core` cục bộ), `npx` sẽ không tìm thấy binary
cục bộ và tự tải về một package **hoàn toàn khác** tên trùng là `stryker` (bản v1.0.1 cũ,
đã bị khai tử từ 2019) từ npm registry, gây lỗi `Cannot find module 'rx'` và crash ngay.
Luôn đảm bảo đang ở đúng thư mục `frontend-web` trước khi chạy `npx stryker run`, hoặc gọi
trực tiếp `./node_modules/.bin/stryker run`.

### Bước 9 — Xem report

Report HTML tạo tại:

```
demo/eshop-sut/frontend-web/reports/mutation/mutation.html
```

Bản sao của report này đã được lưu lại tại [`mutation-report/mutation.html`](./mutation-report/mutation.html)
trong thư mục này — mở file bằng trình duyệt để xem chi tiết từng mutant.

### Bước 10 — Mở rộng phạm vi mutate sang `Register.jsx` để tìm ví dụ "Survived"

Bộ test cho `CartContext.jsx` kill 100% mutant có coverage (không có mutant `Survived` thật
sự, chỉ có `NoCoverage`). Để có ví dụ "Survived" kinh điển — tức test *có* chạy qua code
nhưng assertion không đủ mạnh để bắt lỗi — cần một module có test nhưng test đó hời hợt.

Chọn `src/pages/Register.jsx`: hàm `handleSubmit` chứa một regex kiểm tra mật khẩu mạnh
(`flawedStrongPasswordRegex`, dòng 15) — bản thân regex này **đã bị cài lỗi cố ý** trong SUT
(yêu cầu khoảng trắng `\s` thay vì ký tự đặc biệt, dù thông báo lỗi ghi "ký tự đặc biệt").

Viết test tối thiểu — kiểu test hay gặp trong thực tế: chỉ thử **một** input không hợp lệ rồi
coi như xong — `test/pages/Register.test.jsx`:

```jsx
import { describe, it, expect } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import Register from '../../src/pages/Register';

function renderRegister() {
  const utils = render(
    <MemoryRouter>
      <Register />
    </MemoryRouter>,
  );
  const passwordInput = utils.container.querySelector('input[type="password"]');
  const form = utils.container.querySelector('form');
  return { ...utils, passwordInput, form };
}

describe('Register - password validation', () => {
  it('shows an error when the password is too weak', () => {
    const { passwordInput, form } = renderRegister();

    fireEvent.change(passwordInput, { target: { value: 'abc' } });
    fireEvent.submit(form);

    expect(screen.getByText(/Mật khẩu quá yếu/i)).toBeInTheDocument();
  });
});
```

Cập nhật `stryker.conf.json`:

```json
{
  "$schema": "./node_modules/@stryker-mutator/core/schema/stryker-schema.json",
  "packageManager": "npm",
  "testRunner": "vitest",
  "reporters": ["html", "clear-text", "progress", "json"],
  "coverageAnalysis": "perTest",
  "mutate": ["src/context/CartContext.jsx", "src/pages/Register.jsx"]
}
```

(Thêm reporter `json` để có thể phân tích số liệu chính xác theo từng loại mutator bằng
script, không chỉ đọc bảng tổng hợp trên terminal.)

Chạy lại:

```bash
./node_modules/.bin/stryker run
```

## 5. Kết quả thực tế (sau khi mở rộng sang Register.jsx)

```
------------------|------------------|----------|-----------|------------|----------|----------|
                  | % Mutation score |          |           |            |          |          |
File              |  total | covered | # killed | # timeout | # survived | # no cov | # errors |
------------------|--------|---------|----------|-----------|------------|----------|----------|
All files         |  33.33 |   42.55 |       20 |         0 |         27 |       13 |        0 |
 context          |  85.71 |  100.00 |       12 |         0 |          0 |        2 |        0 |
  CartContext.jsx  |  85.71 |  100.00 |       12 |         0 |          0 |        2 |        0 |
 pages             |  17.39 |   22.86 |        8 |         0 |         27 |       11 |        0 |
  Register.jsx     |  17.39 |   22.86 |        8 |         0 |         27 |       11 |        0 |
------------------|--------|---------|----------|-----------|------------|----------|----------|
```

- **`CartContext.jsx`: 85.71%** — test kill hết phần có coverage (100%), chỉ mất điểm vì
  `removeFromCart` chưa được test (`NoCoverage`).
- **`Register.jsx`: 17.39%** — đây là file có **mutation score thấp và survived cao**, dù
  file này **có** test và test đó **pass**. Đúng dạng "coverage có, chất lượng test không có"
  mà bài seminar cần minh hoạ.

## 6. Phân tích chi tiết Survived mutants — `Register.jsx` (27 survived / 46 total)

Số liệu trích chính xác từ `mutation-report/mutation.json` (đếm theo `status` + `mutatorName`):

| Loại mutant (mutator) | Vị trí | Số survived | Vì sao survived — thiếu test case gì |
|---|---|---|---|
| `Regex` | dòng 15, biểu thức `flawedStrongPasswordRegex` | **18** | Test chỉ thử **một** password `"abc"` (rỗng mọi điều kiện). Gần như mọi biến thể mutate của regex (đảo lookahead, đổi `[a-z]`↔`[^a-z]`, bỏ `*`, đổi `{8,}`, đổi `\s`↔`\S`...) **vẫn** khiến `"abc"` bị từ chối → test vẫn pass dù regex đã sai. Thiếu test theo từng điều kiện riêng lẻ (thiếu hoa, thiếu thường, thiếu số, thiếu khoảng trắng, đúng/sai biên độ dài 8 ký tự) và **thiếu test với password hợp lệ**. |
| `StringLiteral` | dòng 6-9, `useState('')` của name/email/password | **4** | Test không bao giờ assert giá trị khởi tạo của input (`''` → `"Stryker was here!"` vẫn không bị phát hiện) vì không có test kiểm tra state ban đầu / giá trị hiển thị lúc mới render. |
| `ArrowFunction` | dòng 40, 50, 60 — `onChange` của name/email/password | **3** | Test chỉ tương tác với ô password; kể cả `onChange` của chính ô password khi bị thay bằng no-op cũng survive, vì password rỗng (`''`, do onChange không còn set state) vẫn trượt regex như password `"abc"` — kết quả hiển thị lỗi giống hệt nên test không phân biệt được. |
| `ConditionalExpression` | dòng 17, `if (!regex.test(password))` → `if (true)` | **1** | Test **chưa từng thử password hợp lệ**. Ép điều kiện luôn đúng (luôn báo lỗi) không ảnh hưởng gì vì test luôn kỳ vọng có lỗi. Thiếu test "password hợp lệ thì KHÔNG hiện lỗi". |
| `LogicalOperator` | dòng 33, `{error && <div>...}` → `{error \|\| <div>...}` | **1** | `&&` và `\|\|` cho kết quả giống nhau khi `error` đang truthy (test chỉ kiểm tra lúc có lỗi). Thiếu test khẳng định **không có** div lỗi khi chưa submit / khi input hợp lệ. |

**Kết luận cho slide/báo cáo:** Test suite của `Register.jsx` có 1 test case, test đó **pass**
và **có coverage** (22.86% mutant có coverage, không phải 0% như no-coverage), nhưng vì chỉ
kiểm tra đúng 1 kịch bản (password hoàn toàn rỗng nội dung) và chỉ assert 1 điều (có xuất
hiện thông báo lỗi), nên 27/35 mutant có coverage vẫn sống sót — mutation score trong phần có
coverage chỉ 22.86%, thấp hơn nhiều so với 100% của `CartContext.jsx`. Đây là bằng chứng thực
nghiệm rõ ràng cho luận điểm chính của đề tài: **code coverage cao (hoặc test pass) không
đồng nghĩa test suite có khả năng phát hiện lỗi logic.**

## 6b. Viết thêm test để kill các mutant Survived — kết quả trước/sau

Bổ sung `test/pages/Register.test.jsx` thành bộ test đầy đủ hơn (đã lưu thật trong repo demo),
theo đúng 3 nhóm đề xuất ở mục 6:

1. **Test trạng thái ban đầu** — mọi field rỗng, chưa có khối lỗi (`.bg-red-100`) trước khi
   submit → kill mutant `LogicalOperator` (`error && <div>` → `error || <div>`) và các
   `StringLiteral` trên giá trị khởi tạo `useState('')`.
2. **Test từng điều kiện riêng lẻ của regex** — thiếu hoa, thiếu thường, thiếu số, thiếu
   khoảng trắng, đúng 7 ký tự (thiếu độ dài) — mỗi test chỉ sai đúng 1 điều kiện để cô lập
   từng lookahead trong regex.
3. **Test password hợp lệ (boundary đúng 8 ký tự)** — không hiện lỗi, gọi đúng
   `axios.post('http://localhost:3000/api/register', { name, email, password })` (assert cả
   URL lẫn payload, không chỉ "có gọi axios").
4. **Test cập nhật input Họ Tên / Email** → kill mutant `ArrowFunction` trên `onChange`.

Kết quả đo được qua 3 lần chạy Stryker (mutate cả `CartContext.jsx` lẫn `Register.jsx`):

| Lần chạy | Số test case (Register) | Mutation score `Register.jsx` | Survived |
|---|---|---|---|
| 1 — chỉ 1 test hời hợt | 1 | **17.39%** | 27 |
| 2 — thêm test theo từng điều kiện + password hợp lệ + input name/email | 9 | **60.87%** | 11 |
| 3 — thêm assertion "không có khối lỗi lúc đầu" + assert đúng payload `axios.post` | 9 (siết assertion) | **76.09%** | 4 |

Mutation score tăng từ **17.39% → 76.09%** chỉ bằng cách viết thêm/siết test, **không sửa một
dòng code nào** — đúng minh hoạ trực quan nhất cho khái niệm Test Effectiveness.

**4 mutant vẫn còn Survived sau cùng** (không kill hết 100%, đây là kết quả thật, không làm
tròn):

| Mutator | Mutant | Vì sao vẫn sống |
|---|---|---|
| `Regex` | bỏ anchor `$` cuối regex | Mọi chuỗi test đều "sạch" (không có ký tự thừa sau đoạn hợp lệ), nên có hay không có `$` không tạo ra khác biệt quan sát được. Muốn kill cần test chuỗi có ký tự thừa **sau** đoạn hợp lệ, ví dụ `"Abcdef1 !!!"`. |
| `Regex` | bỏ anchor `^` đầu regex | Tương tự — cần test chuỗi có ký tự thừa **trước** đoạn hợp lệ, ví dụ `"!!!Abcdef1 "`. |
| `Regex` | đổi `.*[a-z]` (lookahead đầu) thành `.[a-z]` | Khác biệt cực nhỏ giữa "có ký tự bất kỳ ngay trước chữ thường" và "có ký tự bất kỳ (0 hoặc nhiều) trước chữ thường" — với các chuỗi test hiện tại, chữ thường luôn xuất hiện đủ sớm nên không phân biệt được. Cần input mà chữ thường nằm ở vị trí xa đầu chuỗi. |
| `StringLiteral` | `navigate('/login')` → `navigate('')` | Test "password hợp lệ" chỉ assert `axios.post` được gọi đúng tham số, chưa assert điều hướng sau khi đăng ký thành công. Cần mock `useNavigate` (từ `react-router-dom`) và assert nó được gọi với `'/login'`. |

Đây là ví dụ thực tế cho việc **mutation testing không nhất thiết phải đạt 100%** — 3/4 mutant
còn lại là các biến thể regex rất tinh vi (anchor/quantifier ở biên), đòi hỏi thiết kế test
case chuyên sâu hơn (fuzzing biên chuỗi), phù hợp để nói về **chi phí/lợi ích** khi đẩy
mutation score lên rất cao (điểm đã nêu trong `tool-survey/tool-survey-strykerjs-jest.md`,
mục Giới hạn).

### Bước 11 — Dời toàn bộ file test ra thư mục `test/` riêng

Ban đầu các file test được viết colocated cùng source (`src/context/CartContext.test.jsx`,
`src/pages/Register.test.jsx`, `src/setupTests.js`) — tiện lúc viết nhanh nhưng khó kiểm soát
khi số lượng test tăng lên. Dời sang thư mục `test/` riêng, mirror lại cấu trúc `src/`:

```bash
mkdir -p test/context test/pages
mv src/context/CartContext.test.jsx test/context/CartContext.test.jsx
mv src/pages/Register.test.jsx      test/pages/Register.test.jsx
mv src/setupTests.js                test/setupTests.js
```

Cập nhật 2 chỗ bị ảnh hưởng:

1. **Import path trong từng file test** — vì file test không còn nằm cùng thư mục với source
   nữa, phải trỏ về `src/` qua đường dẫn tương đối:
   - `test/context/CartContext.test.jsx`: `from '../../src/context/CartContext'`
   - `test/pages/Register.test.jsx`: `from '../../src/pages/Register'`
2. **`vite.config.js`** — cập nhật `setupFiles`:

```js
test: {
  environment: 'jsdom',
  globals: true,
  setupFiles: './test/setupTests.js',
},
```

Không cần sửa `stryker.conf.json` — trường `mutate` chỉ liệt kê file **source** cần mutate
(`src/context/CartContext.jsx`, `src/pages/Register.jsx`), không liên quan tới vị trí file
test. Vitest mặc định tự tìm mọi file khớp `**/*.test.{js,jsx,ts,tsx}` trong toàn bộ project
nên không cần khai báo thêm `include`.

Cấu trúc thư mục sau khi dời:

```
frontend-web/
├── src/
│   ├── context/
│   │   ├── AuthContext.jsx
│   │   └── CartContext.jsx        (không còn file .test.jsx ở đây)
│   └── pages/
│       ├── Register.jsx
│       └── ...                    (không còn file .test.jsx ở đây)
├── test/
│   ├── setupTests.js
│   ├── context/
│   │   └── CartContext.test.jsx
│   └── pages/
│       └── Register.test.jsx
├── vite.config.js
└── stryker.conf.json
```

Chạy lại `npm test` và `./node_modules/.bin/stryker run` để xác nhận — kết quả thật đo được
**không đổi** so với trước khi dời (78.33% tổng / 85.71% CartContext.jsx / 76.09%
Register.jsx), chứng tỏ việc tổ chức lại thư mục test không ảnh hưởng tới mutation testing.

### Bước 12 — Tự động xuất `strykerjs-report.md` mỗi khi chạy `stryker run`

StrykerJS **không có sẵn reporter dạng Markdown** (danh sách reporter chính thức chỉ có:
`html`, `clear-text`, `dashboard`, `dots`, `event-recorder`, `json`, `mocha`, `progress`,
`progress-append-only`, `teamcity`; đã kiểm tra trên npm registry, cũng không có package cộng
đồng nào tên `stryker-markdown-reporter`). Để có file `.md` tự sinh ngay khi chạy
`stryker run` mà không cần thêm lệnh phụ, cách sạch nhất là viết một **custom reporter
plugin** theo đúng API chính thức của Stryker (`@stryker-mutator/api/plugin`), không phải
script hậu xử lý chạy tách rời.

File `stryker-markdown-reporter.js` (đặt cùng cấp `stryker.conf.json`):

```js
import fs from 'fs';
import path from 'path';
import { declareClassPlugin, PluginKind } from '@stryker-mutator/api/plugin';

class MarkdownReporter {
  onMutationTestReportReady(report) {
    // đọc report.files (cùng cấu trúc với reports/mutation/mutation.json),
    // dựng bảng tổng hợp + danh sách survived/no-coverage mutant theo Markdown,
    // rồi ghi ra strykerjs-report.md ở thư mục gốc project.
    // (nội dung đầy đủ nằm trong file thật của repo demo)
  }
}

export const strykerPlugins = [declareClassPlugin(PluginKind.Reporter, 'markdown', MarkdownReporter)];
```

Cách hoạt động: Stryker gọi hook `onMutationTestReportReady(report)` trên **mọi** reporter đã
đăng ký ngay sau khi mutation testing xong — object `report` có cấu trúc giống hệt
`mutation.json` (từng file → danh sách mutant với `status`, `mutatorName`, `replacement`,
`location`). Reporter tự viết đọc `report` này và `fs.writeFileSync` ra file `.md`.

Đăng ký plugin trong `stryker.conf.json`:

```json
{
  "$schema": "./node_modules/@stryker-mutator/core/schema/stryker-schema.json",
  "packageManager": "npm",
  "testRunner": "vitest",
  "plugins": ["@stryker-mutator/*", "./stryker-markdown-reporter.js"],
  "reporters": ["html", "clear-text", "progress", "json", "markdown"],
  "coverageAnalysis": "perTest",
  "mutate": ["src/context/CartContext.jsx", "src/pages/Register.jsx"]
}
```

- `plugins`: mặc định Stryker chỉ tự nạp các package `@stryker-mutator/*` đã cài; muốn nạp
  thêm file plugin tự viết phải khai báo rõ đường dẫn (`"./stryker-markdown-reporter.js"`),
  giữ nguyên `"@stryker-mutator/*"` để không mất các plugin có sẵn (vitest-runner, html/json
  reporter...).
- `reporters`: thêm tên `"markdown"` — đúng tên đã đăng ký ở `declareClassPlugin(...)`.

Chạy `./node_modules/.bin/stryker run` như bình thường — không cần thêm lệnh nào khác. Log
thật xác nhận đã chạy:

```
[MarkdownReporter] wrote E:\...\demo\eshop-sut\frontend-web\strykerjs-report.md
```

Nội dung `strykerjs-report.md` sinh ra khớp 100% với bảng trên terminal và với
`reports/mutation/mutation.json` (đã đối chiếu số liệu):

```
# StrykerJS Mutation Report

## Summary

| File | Total | Killed | Survived | Timeout | No coverage | Score (total) | Score (covered) |
|---|---|---|---|---|---|---|---|
| src/context/CartContext.jsx | 14 | 12 | 0 | 0 | 2 | 85.71% | 100.00% |
| src/pages/Register.jsx | 46 | 35 | 4 | 0 | 7 | 76.09% | 89.74% |
| **All files** | **60** | **47** | **4** | **0** | **9** | **78.33%** | **92.16%** |

## Survived mutants
...
## No-coverage mutants
...
```

Bản đầy đủ đã lưu lại tại [`mutation-report/strykerjs-report.md`](./mutation-report/strykerjs-report.md).

## 7. Ý nghĩa cho seminar (Test Effectiveness)

- `CartContext.jsx` minh hoạ trường hợp **"NoCoverage"**: một hàm (`removeFromCart`) hoàn
  toàn chưa được test — phần có test thì mutation score = 100%.
- `Register.jsx` minh hoạ trường hợp **"Survived"**: có test, test pass, có coverage, nhưng
  ban đầu assertion quá hời hợt (1 test, 1 assertion) nên chỉ kill được 22.86% mutant có
  coverage — đúng loại lỗ hổng mà công cụ đo *code coverage* thuần tuý (Jest Coverage/Istanbul)
  **không thể phát hiện**, vì coverage chỉ quan tâm dòng code có được chạy qua hay không,
  không quan tâm assertion có đủ mạnh hay không.
- `Register.jsx` cũng minh hoạ chiều ngược lại: **viết thêm test có mục tiêu (boundary,
  equivalence class, đủ kịch bản happy/negative path) cải thiện mutation score từ 17.39% lên
  76.09% mà không sửa một dòng code nào** — đây là demo mạnh nhất cho khái niệm Test
  Effectiveness của cả bài seminar.
- Ghi chú: con số ví dụ "mutation score: 40%" nêu ra ban đầu chỉ là minh hoạ; kết quả thật đo
  được cuối cùng là **85.71%** (`CartContext.jsx`, chưa test `removeFromCart`) và **76.09%**
  (`Register.jsx`, sau khi bổ sung test cho phần password), tổng hợp toàn bộ 2 file: **78.33%**
  (47 killed / 4 survived / 9 no-coverage / 60 mutant).

## 8. Việc cần làm tiếp (đề xuất)

- Muốn đẩy `Register.jsx` gần 100%: thêm test cho `removeFromCart` (kill nốt 2 no-coverage ở
  `CartContext.jsx`), thêm test chuỗi có ký tự thừa trước/sau đoạn password hợp lệ (kill 2
  mutant anchor `^`/`$`), và mock `useNavigate` để assert điều hướng `'/login'` (kill mutant
  `StringLiteral` cuối cùng) — chi tiết từng mutant còn sống đã liệt kê ở mục 6b.
- Mở rộng phạm vi `mutate` sang `AuthContext.jsx`, `Login.jsx`, `ForgotPassword.jsx` nếu cần
  thêm số liệu cho slide.
- Lưu ảnh chụp report HTML (mở bằng trình duyệt) vào `evidence/week-05/` theo đúng quy ước
  minh chứng của nhóm.
