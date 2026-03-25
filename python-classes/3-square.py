#!/usr/bin/python3
"""Square with area calculation"""


class Square:
    """Square with area method"""

    def __init__(self, size=0):
        """Initialize square"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Return area of square"""
        return self.__size ** 2
