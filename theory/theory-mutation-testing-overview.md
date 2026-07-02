# Mutation Testing Overview

## 1. Goal

This section explains the basic idea of mutation testing and why it is used to evaluate the quality of a test suite.

Mutation testing focuses on one main question:

> If the source code is changed slightly in a wrong way, can the existing tests detect that change?

## 2. Key Questions

### What is mutation testing?

Mutation testing is a software testing technique used to evaluate test effectiveness. It works by creating small artificial changes in the source code. Each changed version is called a **mutant**.

After mutants are created, the test suite is executed again. If the tests fail, the mutant is considered **killed**. If the tests still pass, the mutant **survives**.

### What problem does it solve?

Mutation testing helps identify weak test cases. A project may have high code coverage, but the tests may still be poor if they do not contain strong assertions or important boundary cases.

Mutation testing solves this problem by checking whether the test suite can detect small logic changes in the code.

## 3. Main Notes

Mutation testing is not mainly used to find bugs in production code. Instead, it is used to measure how strong the test suite is.

The basic idea is:

1. Start with original source code.
2. Make a small change to the code.
3. Run the existing tests.
4. Check whether the tests detect the change.

Common small changes include:

- Changing `>` to `>=`
- Changing `+` to `-`
- Changing `true` to `false`
- Changing `&&` to `||`
- Changing a return value

If many mutants are killed, the test suite is stronger. If many mutants survive, the test suite may be missing important test cases or assertions.

## 4. Example

Original code:

```js
function isAdult(age) {
  return age >= 18;
}
```

Mutant version:

```js
function isAdult(age) {
  return age > 18;
}
```

In this mutant, the operator `>=` is changed to `>`.

If the test suite only checks this case:

```js
expect(isAdult(20)).toBe(true);
```

The mutant may survive because both versions return `true` for `age = 20`.

But if the test suite checks the boundary value:

```js
expect(isAdult(18)).toBe(true);
```

The mutant will be killed because:

- Original code: `18 >= 18` returns `true`
- Mutant code: `18 > 18` returns `false`

This shows that mutation testing can reveal missing boundary tests.

## 5. Key Takeaways

- Mutation testing evaluates the quality of test cases.
- A mutant is a small changed version of the original code.
- A killed mutant means the test suite detected the change.
- A survived mutant means the test suite did not detect the change.
- Mutation testing is useful because high code coverage does not always mean strong tests.
- It helps testers find missing assertions, missing boundary cases, and weak test logic.

## 6. References

- https://stryker-mutator.io/docs/
- https://stryker-mutator.io/docs/mutation-testing-elements/supported-mutators/
- https://testrigor.com/blog/understanding-mutation-testing-a-comprehensive-guide/
