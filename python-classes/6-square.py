#!/usr/bin/python3
"""
This module defines a Square class that supports size, position,
area calculation, and printing with coordinates.
"""


class Square:
    """
    This class represents a square with a size and a position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a Square instance.

        Args:
            size (int): The size of the square.
            position (tuple): The position (x, y) offset.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieve the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieve the position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square with validation.
        """
        if (
            type(value) is not tuple or
            len(value) != 2 or
            type(value[0]) is not int or
            type(value[1]) is not int or
            value[0] < 0 or
            value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """
        Return the area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Print the square using the # character, respecting position.
        """
        if self.__size == 0:
            print()
            return

        # vertical offset
        for _ in range(self.__position[1]):
            print()

        # square rows
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
