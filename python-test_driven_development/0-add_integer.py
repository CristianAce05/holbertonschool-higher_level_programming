#!/usr/bin/python3
"""Module that adds two integers.

This module defines a function to add two numbers.
Numbers can be integers or floats.
Floats are cast to integers before addition.
"""


def add_integer(a, b=98):
    """Add two integers.

    a and b must be integers or floats.
    Returns the integer sum of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
