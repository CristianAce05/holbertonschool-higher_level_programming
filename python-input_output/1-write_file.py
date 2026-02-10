#!/usr/bin/python3
"""1-write_file module

Function that writes a string to a UTF-8 text file and returns
the number of characters written.
"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns number characters.

    Args:
        filename (str): path to the file to write. Defaults to empty string.
        text (str): text to write to the file.

    Returns:
        int: number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
