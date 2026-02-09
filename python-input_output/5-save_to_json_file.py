#!/usr/bin/python3
"""
Module for saving Python objects to a file using JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a text file in JSON format.

    Args:
        my_obj (any): Python object to serialize (e.g., list, dict).
        filename (str): Path to the file where the JSON string will be saved.

    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
