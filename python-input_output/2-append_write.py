#!/usr/bin/python3
"""Appends a string to a UTF-8 text file and returns the number of characters added."""


def append_write(filename="", text=""):
    """Append a string to a text file and return the number of characters written."""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
