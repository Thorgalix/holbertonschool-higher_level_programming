#!/usr/bin/python3
"""
Module for converting JSON representation to Python object.
"""

import json


def from_json_string(my_str):
    """
    Returns the Python object of a JSON representation.

    Args:
        my_str (any): JSON representation.

    Returns:
        object (Python data structure).
    """
    return json.loads(my_str)
