#!/usr/bin/python3
"""
Module that defines the CountedIterator class.

This module provides a wrapper around any iterable, allowing
iteration while keeping track of the number of items accessed.
"""


class CountedIterator:
    """
    Iterator wrapper that counts how many items have been iterated.

    Attributes:
        iterator: The original iterator created from the given iterable.
        count (int): Number of items that have been iterated so far.
    """

    def __init__(self, obj):
        """
        Initialize the CountedIterator with an iterable.

        Args:
            obj: Any iterable object to wrap.
        """
        self.iterator = iter(obj)
        self.count = 0

    def get_count(self):
        """
        Return the number of items iterated so far.

        Returns:
            int: The count of items retrieved by next().
        """
        return self.count

    def __next__(self):
        """
        Return the next item from the iterator and increment the counter.

        Returns:
            The next item from the wrapped iterable.

        Raises:
            StopIteration: When there are no more items to iterate.
        """
        self.count += 1
        return next(self.iterator)
