#!/usr/bin/env python3
"""
This module defines a VerboseList class that extends the built-in list
to print notifications upon modification.
"""


class VerboseList(list):
    """
    A custom list class that prints messages when items are added or removed.
    """

    def append(self, item):
        """Adds an item to the end of the list and prints a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extends the list with items from an iterable and prints a notification."""
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        """Removes the first occurrence of item and prints a notification."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Removes and returns the item at the given index and prints a notification."""
        print(f"Popped [{self[index]}] from the list.")
        return super().pop(index)