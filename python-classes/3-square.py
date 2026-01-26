#!/usr/bin/python3
""" define a class"""


class Square:
    """square class"""

    def __init__(self, size=0):
        """main things in this class"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size
