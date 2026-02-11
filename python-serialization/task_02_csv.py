#!/usr/bin/python3
"""
Module that converts CSV data into JSON format.
"""
import csv
import json


def convert_csv_to_json(filename):
    """
    Converts a CSV file to JSON format and saves the result to 'data.json'.

    This function reads the CSV file specified by filename,
    converts each row into a dictionary using csv.DictReader,
    serializes the data into JSON format, and writes it to
    a file named 'data.json'.

    Args:
        filename (str): The path to the CSV file to convert.

    Returns:
        bool: True if the conversion was successful,
              False if an error occurred (e.g., file not found).
    """
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as csvfile:
            data = list(csv.DictReader(csvfile))
        with open('data.json', mode='w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=4)
        return True

    except FileNotFoundError:
        return False
