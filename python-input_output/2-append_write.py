#!/usr/bin/python3
"""Append text to a UTF-8 file and return the number of characters added."""


def append_write(filename="", text=""):
    """Append text to a file and return the number of characters written."""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
