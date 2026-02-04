#!/usr/bin/python3
"""Module that defines abstract and concrete shape classes using duck typing.

This module provides:
- An abstract base class Shape with abstract methods area and perimeter.
- Concrete implementations: Circle and Rectangle.
- A utility function shape_info that prints the area and perimeter of any shape
  object, relying on duck typing.
"""

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class representing a generic geometric shape.

    Subclasses must implement the area() and perimeter() methods.
    """
    @abstractmethod
    def area(self):
        """Compute and return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Compute and return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Concrete class representing a circle shape."""
    def __init__(self, radius):
        """Initialize a Circle instance.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Concrete class representing a rectangle shape."""
    def __init__(self, width, height):
        """Initialize a Rectangle instance.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Prints the area and perimeter of any shape object."""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
