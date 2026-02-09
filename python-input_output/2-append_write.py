#!/usr/bin/python3
"""
Module for writing text to a file.
"""


def append_write(filename="", text=""):
    """
    Writes a string to a text file (UTF-8) and returns the number of
    characters written.

    Args:
        filename (str): Path to the file to write to.
        text (str): Text to be written to the file.

    Returns:
        int: Number of characters written.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
