#!/usr/bin/python3
""" Script that prints a square with the character #. """


def print_square(size):
    """
    Function that prints a square with the character #.

    Args:
        size (int): The size length of the square.

    Returns:
        None

    Raises:
        TypeError: If 'size' is not an integer,
        or if it is a float less than 0.
        ValueError: If 'size' is less than 0.
    """

    error = "unsupported operand type(s) for +: 'NoneType' and 'int'"

    if size is None:
        raise TypeError(error)
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and type(size) < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
