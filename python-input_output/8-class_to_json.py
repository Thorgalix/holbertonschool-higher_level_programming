#!/usr/bin/python3
"""
Module that provides a function to retrieve the dictionary
representation of a class instance for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary representation of a class instance's
    attributes for JSON serialization.

    Args:
        obj (any): Instance of a class whose attributes are to be
                   retrieved. All attributes should be of type
                   list, dict, str, int, or bool.

    Returns:
        dict: Dictionary containing all instance attributes with
              their names as keys and their values as values.
    """
    return obj.__dict__
