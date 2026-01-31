#!/usr/bin/env python3
"""
This module defines a CountedIterator class that tracks the number of items iterated.
"""


class CountedIterator:
    """
    An iterator that keeps track of how many items have been iterated over.
    """

    def __init__(self, iterable):
        """Initializes the iterator and the counter."""
        self.iterator = iter(iterable)
        self.counter = 0

    def get_count(self):
        """Returns the current number of iterated items."""
        return self.counter

    def __next__(self):
        """
        Fetches the next item from the iterator and increments the counter.
        Raises StopIteration when no items are left.
        """
        item = next(self.iterator)
        self.counter += 1
        return item