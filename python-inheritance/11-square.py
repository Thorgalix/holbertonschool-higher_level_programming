#!/usr/bin/python3
"""Module that defines a Square class that
inherits from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square with validated size."""
    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square (width = height = size).
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
            int: The area (width * height).
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Returns the string representation of the square.

        Format: [Square] <width>/<height>

        Returns:
            str: The rectangle description.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
