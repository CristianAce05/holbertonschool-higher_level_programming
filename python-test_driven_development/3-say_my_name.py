#!/usr/bin/python3
""" Script that prints a full name. """


def say_my_name(first_name, last_name=""):
    """
    Function that prints full name.

    Args:
        first_name (str): The first name to be printed.
        last_name (str, optional): The last name to be printed.
        Defaults to an empty string.

    Returns:
        None

    Raises:
        TypeError: If 'first_name' or 'last_name' is not a string.
    """

    first = "first_name must be a string"
    last = "last_name must be a string"

    if type(first_name) is not str:
        raise TypeError(first)
    if type(last_name) is not str:
        raise TypeError(last)
    if last_name == "":
        print(f"My name is {first_name} ")
    else:
        print(f"My name is {first_name} {last_name}")
