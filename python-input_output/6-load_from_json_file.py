#!/usr/bin/python3
"""Defines a JSON file-writing function."""
import json


def load_from_json_file(filename):
    """func"""
    with open(filename, "r") as f:
        return json.load(f)
