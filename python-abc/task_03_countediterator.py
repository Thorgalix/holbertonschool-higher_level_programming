#!/usr/bin/python3
"""
Module that defines the CountedIterator class.
"""


class CountedIterator:
    """Iterator wrapper that counts how many items have been iterated."""

    def __init__(self, obj):
        """Initialize with an iterable object."""
        self.iterator = iter(obj)
        self.count = 0

    def get_count(self):
        """Return the number of items iterated so far."""
        return (self.count)

    def __next__(self):
        """Return the next item and increment the count."""
        self.count += 1
        return next(self.iterator)

    def __iter__(self):
        """Return self as an iterator."""
        return self
