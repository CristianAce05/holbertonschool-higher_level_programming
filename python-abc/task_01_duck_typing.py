#!/usr/bin/python3
"""Abstract Shape class with Circle and Rectangle implementations, using duck typing."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle shape."""

    def __init__(self, radius):
        # Handle negative radius by taking absolute value
        self.radius = abs(radius)

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle shape."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of a shape using duck typing."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


# --- Testing ---
if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    circle_negative = Circle(-5)

    print("Circle info:")
    shape_info(circle)
    print("\nRectangle info:")
    shape_info(rectangle)
    print("\nNegative radius circle info:")
    shape_info(circle_negative)
