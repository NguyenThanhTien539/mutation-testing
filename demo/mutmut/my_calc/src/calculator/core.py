def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0: raise ValueError("Cannot divide by zero.")
    return a / b
def exponentiate(a, b): return a ** b

def solve_linear_equation(func, y, guess=0, tolerance=1e-7):
    """
    Solves f(x) = y using the bisection method.
    func: a function f(x)
    y: the target value
    """
    # This finds root of f(x) - y = 0
    low, high = -1000, 1000
    for _ in range(100):
        mid = (low + high) / 2
        val = func(mid) - y
        if abs(val) < tolerance:
            return mid
        if val > 0: high = mid
        else: low = mid
    return mid