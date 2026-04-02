#!/usr/bin/python3
"""Reads a file and prints it"""


def read_file(filename=""):
    """Read and print file content"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
