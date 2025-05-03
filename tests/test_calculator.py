import pytest
from app import calculator

def test_add():
    assert calculator.add(2, 3) == 5

def test_subtract():
    assert calculator.subtract(5, 2) == 3

def test_multiply():
    assert calculator.multiply(3, 4) == 12

def test_divide():
    assert calculator.divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        calculator.divide(10, 0)
