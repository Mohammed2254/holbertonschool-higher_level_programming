#!/usr/bin/python3
"""module"""

class Student:

    """class"""
    def __init__(self, first_name, last_name, age):
        """main obj"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """to"""
        return self.__dict__
