#!/usr/bin/python3
"""
Module for basic serialization and deserialization of Python dictionaries
using JSON files.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary and saves it to a JSON file.

    Args:
        data (dict): The Python dictionary to serialize.
        filename (str): The name of the file where the JSON data
                        will be saved. If the file exists, it will
                        be overwritten.

    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Loads and deserializes JSON data from a file into a Python dictionary.

    Args:
        filename (str): The name of the JSON file to read from.

    Returns:
        dict: The Python dictionary obtained from the deserialized JSON data.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
