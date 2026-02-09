#!/usr/bin/python3
"""
Module for converting Python objects to JSON strings.
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of a Python object.

    Args:
        my_obj (any): Python object to convert (e.g., dict, list, etc.).

    Returns:
        str: JSON string representation of the object.
    """
    return json.dumps(my_obj)
