#!/usr/bin/python3
"""
Module that defines the VerboseList class, which extends
Python's built-in list with notifications on modifications.
"""


class VerboseList(list):
    """
    A subclass of list that prints a message whenever an item
    is added, removed, or popped, or when the list is extended.
    """
    def append(self, item):
        """
        Add an item to the list and print a notification.

        Args:
            item: The element to be appended to the list.
        """
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """
        Extend the list by appending elements from the iterable
        and print a notification with the number of items added.

        Args:
            iterable: An iterable with elements to add to the list.
        """
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(len(iterable)))

    def remove(self, item):
        """
        Remove the first occurrence of item from the list and
        print a notification before removal.

        Args:
            item: The element to remove from the list.
        """
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """
        Remove and return item at index (default last) and
        print a notification before removal.

        Args:
            index: The position of the item to remove (default: -1).

        Returns:
            The item that was removed.
        """
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        super().pop(index)
