# StrykerJS Mutation Report

_Generated: 2026-07-11T03:15:28.431Z_

## Summary

| File | Total | Killed | Survived | Timeout | No coverage | Score (total) | Score (covered) |
|---|---|---|---|---|---|---|---|
| src/context/CartContext.jsx | 14 | 12 | 0 | 0 | 2 | 85.71% | 100.00% |
| src/pages/Register.jsx | 46 | 35 | 4 | 0 | 7 | 76.09% | 89.74% |
| **All files** | **60** | **47** | **4** | **0** | **9** | **78.33%** | **92.16%** |

## Survived mutants

### src/pages/Register.jsx

- line 15 — **Regex**: `/^(?=.[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\s)[A-Za-z\d\s]{8,}$/`
- line 15 — **Regex**: `/(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\s)[A-Za-z\d\s]{8,}$/`
- line 15 — **Regex**: `/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\s)[A-Za-z\d\s]{8,}/`
- line 24 — **StringLiteral**: `""`

## No-coverage mutants

### src/context/CartContext.jsx

- line 12 — **BlockStatement**: `{}`
- line 13 — **ArrayDeclaration**: `[]`

### src/pages/Register.jsx

- line 25 — **BlockStatement**: `{}`
- line 26 — **ConditionalExpression**: `true`
- line 26 — **ConditionalExpression**: `false`
- line 26 — **LogicalOperator**: `err.response?.data?.error && 'Đăng ký thất bại.'`
- line 26 — **OptionalChaining**: `err.response?.data.error`
- line 26 — **OptionalChaining**: `err.response.data`
- line 26 — **StringLiteral**: `""`
