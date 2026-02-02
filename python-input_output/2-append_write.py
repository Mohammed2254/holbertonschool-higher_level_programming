#!/usr/bin/python3
"""
This module defines a function that appends a string to a text file.
"""


def append_write(filename="", text=""):
    """a func"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
