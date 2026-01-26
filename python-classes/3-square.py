#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:  # Classe
    """Class that defines a square."""
    def __init__(self, size=0):  # Méthode
        """Initializes a square with a given size.

        Args:
            size: The size of the square (must be an integer and >= 0).
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size  # Attribut

    def area(self):
        """Computes and returns the area of the square.

        The area is calculated using the size of the square
        multiplied by itself.
        """
        return self.__size * self.__size
