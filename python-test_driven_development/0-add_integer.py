#!/usr/bin/python3
"""Script that adds two integers"""


def add_integer(a, b=98):
    """
    Function that adds two integers.
    Args:
        a: The first number, must be an integer or float.
        b: The second number, must be an integer or float, defaults to 98.
    Returns:
        The sum of the two numbers as an integer.
    Raises:
        TypeError: If a or b is not an integer or float, or if they are None.
    """
    error = "unsupported operand type(s) for +: 'NoneType' and 'int'"
    if a is None or b is None:
        raise TypeError(error)
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
