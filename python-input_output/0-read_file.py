#!/usr/bin/python3
""" a model that reads a file """


def read_file(filename=""):
    """the func for reading the file succesfully"""
    with open(filename, encoding="UTF-8") as file:
        print(file.read(), end="")
