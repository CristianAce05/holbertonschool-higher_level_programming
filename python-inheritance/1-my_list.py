#!/usr/bin/python3
"""This module defines a MyList class that inherits from list."""


class MyList(list):
    """A custom list class with a method to print the list sorted."""

    def print_sorted(self):
        """Prints the list sorted in ascending order."""
        print(sorted(self))
