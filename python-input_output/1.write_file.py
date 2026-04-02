#!/usr/bin/python3
"""Writes to a file"""


def write_file(filename="", text=""):
    """Write text to file and return number of chars"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
