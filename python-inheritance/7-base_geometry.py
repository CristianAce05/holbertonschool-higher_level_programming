#!/usr/bin/python3
"""
This module defines a BaseGeometry class with area and
integer validation functionality.
"""


class BaseGeometry:
    """
    This class defines basic geometry methods.
    """

    def area(self):
        """
        Raises an Exception indicating that the area method
        is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is an integer greater than zero.

        Args:
            name (str): The name of the value.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to zero.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
