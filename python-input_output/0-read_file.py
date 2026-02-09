#!/usr/bin/python3
"""
Module for reading and printing the content of a text file.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints its content to stdout.

    Args:
        filename (str): Path to the file to be read.
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read())
