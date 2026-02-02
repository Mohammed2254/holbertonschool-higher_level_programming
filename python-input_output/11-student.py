"""module"""


class Student:
    """class"""

    def __init__(self, first_name, last_name, age):
        """main"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """json things"""
        if isinstance(attrs, list):
            if all(isinstance(x, str) for x in attrs):
                newdict = {}
                for item in attrs:
                    if item in self.__dict__:
                        newdict[item] = self.__dict__[item]
                return newdict

        return self.__dict__

    def reload_from_json(self, json):
        """reload"""
        for key, value in json.items():
            setattr(self, key, value)
