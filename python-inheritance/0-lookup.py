#!/usr/bin/python3
"""Returns the list of available attributes and methods of an object."""


def lookup(obj):
    """
        Returns a list of attributes and methods available for an object.

        Args:
        obj: Any Python object.

        Returns:
        list: List of attribute and method names.
    """
    return dir(obj)
