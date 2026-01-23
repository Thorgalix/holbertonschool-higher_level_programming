#!/usr/bin/python3
"""
    Module 4-print_square: Contient une fonction qui affiche
    un carré de #
"""


def print_square(size):
    """
        Prints a square with the character '#'.

        Args:
            size (int): The size length of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        Description:
            If size is 0, the function does not print anything.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        return
    for i in range(size):
        print("#" * size)
