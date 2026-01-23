#!/usr/bin/python3
""" This script divides each number in a matrix by the given number"""


def matrix_divided(matrix, div):
    """
    Function that divides each number in a matrix by the given number.

    Args:
        matrix: A list of lists containing integers or floats.
        div: The number to divide by (must be integer or float).

    Returns:
        A new matrix with the result of the div rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix contains non-numeric values
        or if div is not a number.
        TypeError: If the rows of the matrix are not all the same size.
        ZeroDivisionError: If div is zero.
    """
    error = "matrix must be a matrix (list of lists) of integers/floats"

    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for rows in matrix:
        if type(rows) is not list:
            raise TypeError(error)
        if len(rows) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for index in rows:
            if type(index) not in (int, float):
                raise TypeError(error)
    return ([list(map(lambda x: round(x / div, 2), rows)) for rows in matrix])
