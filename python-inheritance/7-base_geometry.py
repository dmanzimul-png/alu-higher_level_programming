#!/usr/bin/python3
"""Module that defines BaseGeometry class"""


class BaseGeometry:
    """Base geometry class"""

    def area(self):
        """Raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates integer"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
