#!/usr/bin/python3
"""
Module 5-text_indentation: Contient une fonction qui indente
des retours à la ligne à chaque . ? :
"""


def text_indentation(text):
    """
    Prints a text with a new line after each occurrence of '.', '?' or ':'.

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If text is not a string.

    Description:
        Each printed line will have no spaces at the beginning or end.
        If the text does not end with a separator (., ?, :), the last portion
        of the text is printed on its own line.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    line = ""
    for i, char in enumerate(text):
        line += char
        if char in ".?:":
            print(line.strip())
            if i != len(text) - 1:
                print()
            line = ""
    if line:
        print(line.strip())
