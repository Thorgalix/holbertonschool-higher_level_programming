#!/usr/bin/python3
"""
Module for loading Python objects from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    Creates a Python object from a JSON file.

    Args:
        filename (str): Path to the JSON file to read.

    Returns:
        any: Python object deserialized from the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
