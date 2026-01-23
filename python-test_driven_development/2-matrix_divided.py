#!/usr/bin/python3
"""Module that divides all elements of a matrix."""

def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div.

    Returns a new matrix with results rounded to 2 decimal places.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])

    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
