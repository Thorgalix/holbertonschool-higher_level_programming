#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:  # Classe
    """Class that defines a square."""
    def __init__(self, size=0):  # Méthode
        """Initializes a square with a given size.

        Args:
            size: The size of the square (must be an integer and >= 0).
        """
        self.size = size

    def area(self):
        """Computes and returns the area of the square.

        The area is calculated using the size of the square
        multiplied by itself.
        """
        return self.size * self.size

    @property
    def size(self):
        """Getter for the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size of the square.

        Args:
            value (int): size of the square, must be >= 0

        Raises:
            TypeError: if value is not an integer
            ValueError: if value < 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value  # Attribut privé
