# StrykerJS — Hướng dẫn setup trước khi chạy `stryker run`


## 1. Mục tiêu & phạm vi

Setup StrykerJS để chạy mutation testing trên phân hệ **frontend-web** (React + Vite) của SUT
[`eshop-sut`](https://github.com/KidCute1412/eshop-sut). Test runner dùng **Vitest** (không
phải Jest) vì `frontend-web` đã dùng Vite sẵn — Vitest tái dùng luôn cấu hình Vite, không cần
setup transform/babel riêng.

## 2. Cài đặt dependencies

```bash
cd demo/strykerjs/eshop-sut/frontend-web
npm install -D vitest@4.1.10 jsdom@29.1.1 \
  @testing-library/react@16.3.2 @testing-library/jest-dom@6.9.1 \
  @stryker-mutator/core@9.6.1 @stryker-mutator/vitest-runner@9.6.1
```

## 3. Bật test environment trong `vite.config.js`

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

## 4. Tạo `test/setupTests.js`

```js
import '@testing-library/jest-dom/vitest';
```

## 5. Thêm script `test` vào `package.json`

```json
"scripts": {
  "dev": "vite",
  "build": "vite build",
  "lint": "eslint .",
  "preview": "vite preview",
  "test": "vitest run"
}
```

## 6. Cấu trúc thư mục test

Toàn bộ file test đặt trong thư mục `test/` riêng, **mirror** lại cấu trúc `src/` (không
colocate `*.test.jsx` cạnh source) để dễ kiểm soát khi số lượng test tăng lên:

```
frontend-web/
├── src/
│   ├── context/
│   │   ├── AuthContext.jsx
│   │   └── CartContext.jsx        (không có file .test.jsx ở đây)
│   └── pages/
│       ├── Register.jsx
│       └── ...                    (không có file .test.jsx ở đây)
├── test/
│   ├── setupTests.js
│   ├── context/
│   │   └── CartContext.test.jsx
│   └── pages/
│       └── Register.test.jsx
├── vite.config.js
└── stryker.conf.json
```

Vitest mặc định tự tìm mọi file khớp `**/*.test.{js,jsx,ts,tsx}` trong toàn bộ project, nên
không cần khai báo thêm `include` trong config.

## 7. Viết test tối thiểu cho các module sẽ mutate

Trước khi cấu hình Stryker, mỗi module nằm trong phạm vi `mutate` phải có ít nhất một test
file tương ứng và **test suite phải pass sạch** (baseline). Chi tiết nội dung/thiết kế của
từng test case cho `CartContext.jsx` và `Register.jsx` xem
[`stryker-test-scenario.md`](./stryker-test-scenario.md).

Chạy baseline trước khi đụng tới Stryker:

```bash
npm test
```

Test suite phải pass sạch trước khi chạy Stryker — Stryker cần baseline ổn định để so sánh.

## 8. Tạo `stryker.conf.json`

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

Giải thích từng field:

- `mutate`: giới hạn phạm vi mutate chỉ những file cần đo (project lớn nên luôn giới hạn phạm
  vi — điểm yếu này đã ghi nhận ở `tool-survey/tool-survey-strykerjs-jest.md`).
- `coverageAnalysis: "perTest"`: Stryker dùng coverage để biết mutant nào được test nào chạy
  qua, giúp chạy nhanh hơn (chỉ chạy các test có liên quan tới mutant đó).
- `reporters`: `"html"` sinh report HTML tại `reports/mutation/mutation.html`; `"json"` sinh
  `reports/mutation/mutation.json` để phân tích số liệu chính xác theo từng loại mutator bằng
  script (không chỉ đọc bảng tổng hợp trên terminal); `"clear-text"`/`"progress"` in tiến độ
  ra terminal.
- `plugins`: mặc định Stryker chỉ tự nạp các package `@stryker-mutator/*` đã cài; muốn nạp
  thêm plugin tự viết phải khai báo rõ đường dẫn.


## 9. Checklist trước khi chạy `stryker run`

- [ ] `npm install` đã cài đủ dependencies ở mục 2.
- [ ] `vite.config.js` đã có `test.setupFiles` trỏ đúng `./test/setupTests.js`.
- [ ] `npm test` chạy **pass sạch, không lỗi** (baseline bắt buộc).
- [ ] `stryker.conf.json` tồn tại, `mutate` liệt kê đúng các file **source** cần đo (không
      liên quan tới vị trí file test).
- [ ] Đang đứng đúng trong thư mục `demo/strykerjs/eshop-sut/frontend-web` (nơi đã cài
      `@stryker-mutator/core` cục bộ).

## 10. Chạy Stryker

```bash
npx stryker run
```

hoặc chắc chắn hơn thì chạy: 

```bash
./node_modules/.bin/stryker run
```

Sau khi chạy xong, report được ghi ra:

- HTML: `reports/mutation/mutation.html`
- JSON: `reports/mutation/mutation.json`