#!/usr/bin/python3
"""Module that defines BaseGeometry class"""


class BaseGeometry:
    """Base geometry class"""

    def area(self):
        """Raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
    """Validates integer"""

    if not isinstance(value, int) or isinstance(value, bool):
        raise TypeError("{} must be an integer".format(name))

    if value <= 0:
        raise ValueError("{} must be greater than 0".format(name))
