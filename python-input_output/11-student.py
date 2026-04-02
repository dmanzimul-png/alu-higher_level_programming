#!/usr/bin/python3
"""Student class with reload"""


class Student:
    """Defines student"""

    def __init__(self, first_name, last_name, age):
        """Initialize"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary"""
        if isinstance(attrs, list):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace attributes"""
        for key, value in json.items():
            setattr(self, key, value)
