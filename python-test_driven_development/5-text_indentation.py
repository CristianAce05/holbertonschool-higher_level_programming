#!/usr/bin/python3
""" Indents given text based on specified punctuation. """


def text_indentation(text):
    """
    Function that prints text with two new lines
    after each of these characters: '.', '?', and ':'.

    Args:
        text (str): The text to be processed.

    Returns:
        None

    Raises:
        TypeError: If 'text' is not a string or if 'text' is empty.
    """
    error = "text_indentation() missing 1 required positional argument: 'text'"
    if text is None:
        raise TypeError(error)
    if type(text) is not str:
        raise TypeError("text must be a string")
    if not text:
        raise TypeError("Text is empty")
    c = 0
    while c < len(text):
        print(text[c], end="")
        if text[c] in ".?:":
            print("\n")
            while c + 1 < len(text) and text[c + 1] == " ":
                c += 1
        c += 1
