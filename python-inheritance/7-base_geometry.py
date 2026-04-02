#!/usr/bin/python3
"""Module that defines BaseGeometry class"""


class BaseGeometry:
    """Base geometry class"""

    def area(self):
        """Raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates integer"""

        if not isinstance(name, str):
            raise TypeError("name must be a string")

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
