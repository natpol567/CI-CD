"""
Testy jednostkowe.
"""

import pytest
from src.utils import add, subtract, multiply, divide


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (0, 0, 0),
        (-1, 1, 0),
    ],
)
def test_add(a, b, expected):
    """Test funkcji add."""
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (5, 3, 2),
        (0, 0, 0),
        (-1, -1, 0),
    ],
)
def test_subtract(a, b, expected):
    """Test funkcji substract."""
    assert subtract(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 6),
        (0, 10, 0),
        (-1, -1, 1),
    ],
)
def test_multiply(a, b, expected):
    """Test funkcji multiply"""
    assert multiply(a, b) == expected


def test_divide_by_zero():
    """Test funkcji divide"""
    with pytest.raises(ValueError):
        divide(1, 0)
