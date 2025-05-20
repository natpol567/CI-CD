"""
Moduł zawiera podstawowe funkcje matematyczne:
add, subtract, multiply, divide.
"""


def add(a, b):
    """
    Zwraca sumę dwóch liczb.
    """
    return a + b


def subtract(a, b):
    """
    Zwraca różnicę dwóch liczb.
    """
    return a - b


def multiply(a, b):
    """
    Zwraca iloczyn dwóch liczb.
    """
    return a * b


def divide(a, b):
    """
    Dzieli a przez b.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
