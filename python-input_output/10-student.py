#!/usr/bin/python3
"""
Module that defines a Student class with JSON serialization support.
"""


class Student:
    """
    Represents a student with first name, last name, and age.

    Attributes:
        first_name (str): The student's first name.
        last_name (str): The student's last name.
        age (int): The student's age.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): First name of the student.
            last_name (str): Last name of the student.
            age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        If attrs is a list of strings, only attributes with names contained
        in this list will be included in the returned dictionary.
        Otherwise, all instance attributes are returned.

        Args:
            attrs (list, optional): List of attribute names to retrieve. Defaults to None.

        Returns:
            dict: Dictionary containing the selected instance attributes.
        """
        attributs = self.__dict__
        if not isinstance(attrs, list):
            return attributs
        filtered_attrs = {}
        for name in attrs:
            if name in attributs:
                filtered_attrs[name] = attributs[name]
        return filtered_attrs
