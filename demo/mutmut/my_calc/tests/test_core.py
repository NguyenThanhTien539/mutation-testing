import sys
import os

# Add the 'src' directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
from calculator.core import add, subtract, multiply, divide, exponentiate, solve_linear_equation

def test_arithmetic():
    assert add(10, 5) == 15
    assert subtract(10, 5) == 5
    assert multiply(10, 5) == 50
    assert divide(10, 2) == 5
    assert exponentiate(2, 3) == 8

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        divide(10, 0)

def test_solve_linear_equation():
    # Solve 2x + 5 = 15 -> 2x = 10 -> x = 5
    f = lambda x: 2 * x + 5
    result = solve_linear_equation(f, 15)
    assert result == pytest.approx(5, abs=1e-5)

def test_complex_combination():
    # Solve (x * 3) / 2 - 4 = 2 -> 1.5x = 6 -> x = 4
    f = lambda x: (multiply(x, 3) / 2) - 4
    result = solve_linear_equation(f, 2)
    assert result == pytest.approx(4, abs=1e-5)

def test_solve_linear_equation_full_iterations():
    # Use a function that doesn't converge perfectly to 0 within tolerance
    # This forces the loop to exhaust all 100 iterations
    f = lambda x: x * 1.0000000000001 # A function that barely changes
    # Setting a target that is hard to hit forces full loop execution
    result = solve_linear_equation(f, 0, tolerance=1e-20) 
    assert isinstance(result, float)
    