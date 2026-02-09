#!/usr/bin/python3
"""
Module for demonstrating pickling of a custom Python class.
Contains the CustomObject class with serialization and deserialization.
"""

import pickle


class CustomObject:
    """
    Represents a custom object with a name, age, and student status.

    Attributes:
        name (str): The name of the object.
        age (int): The age of the object.
        is_student (bool): Whether the object represents a student.
    """
    def __init__(self, name, age, is_student):
        """
        Initializes a CustomObject instance.

        Args:
            name (str): The name of the object.
            age (int): The age of the object.
            is_student (bool): Student status of the object.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Prints the attributes of the object in the following format:

        Name: <name>
        Age: <age>
        Is Student: <True/False>
        """
        print("Name:", self.name)
        print("Age:", self.age)
        print("Is Student:", self.is_student)

    def serialize(self, filename):
        """
        Serializes the current object instance and saves it to a file using
        pickle.

        Args:
            filename (str): The file name where the object will be saved.

        Returns:
            None: If serialization succeeds.
            None: If an exception occurs during serialization.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)

        except (TypeError, OSError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes a CustomObject instance from a file using pickle.

        Args:
            filename (str): The file name from which to load the object.

        Returns:
            CustomObject: The object loaded from the file if successful.
            None: If an exception occurs (file missing or corrupted).
        """
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
            return obj

        except (TypeError, OSError, pickle.PickleError):
            return None
