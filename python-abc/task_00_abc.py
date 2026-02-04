#!/usr/bin/python3
"""
Module that defines an abstract Animal class and its subclasses Dog and Cat.
The Animal class defines a blueprint for all animals with a mandatory
`sound` method.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class representing an animal.

    Methods:
        sound(): Abstract method that should be implemented by subclasses
                  to return the sound the animal makes.
    """
    @abstractmethod
    def sound(self):
        """
        Abstract method to produce the sound of the animal.

        Raises:
            NotImplementedError: Must be implemented by subclasses.
        """
        pass


class Dog(Animal):
    """
    Represents a Dog, subclass of Animal.

    Methods:
        sound(): Returns the sound 'Bark'.
    """
    def sound(self):
        """
        Returns the sound of the dog.

        Returns:
            str: The string "Bark".
        """
        return ("Bark")


class Cat(Animal):
    """
    Represents a Cat, subclass of Animal.

    Methods:
        sound(): Returns the sound 'Meow'.
    """
    def sound(self):
        """
        Returns the sound of the cat.

        Returns:
            str: The string "Meow".
        """
        return ("Meow")
