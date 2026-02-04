#!/usr/bin/python3
"""
Module that defines the CountedIterator class.

This module provides a wrapper around any iterable, allowing
iteration while keeping track of the number of items accessed.
"""


class CountedIterator:
    """
    Iterator wrapper that counts how many items have been iterated.
    """

    def __init__(self, iterable):
        """
        Initialize the CountedIterator with an iterable.

        Args:
            iterable: Any iterable object to wrap.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """
        Return the number of items iterated so far.

        Returns:
            int: Number of items accessed by __next__.
        """
        return self.count

    def __iter__(self):
        """
        Return the iterator object itself.

        Returns:
            self: The iterator instance.
        """
        return self

    def __next__(self):
        """
        Return the next item from the iterator and increment the counter.

        Returns:
            The next item from the wrapped iterable.

        Raises:
            StopIteration: When there are no more items.
        """
        self.count += 1
        return next(self.iterator)
