#!/usr/bin/python3
"""Square with validated size"""


class Square:
    """Square with size validation"""

    def __init__(self, size=0):
        """Initialize square with validation"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
