#!/usr/bin/python3
""" from a class to json"""


def class_to_json(obj):
    """return the obj as a dict"""
    return obj.__dict__
