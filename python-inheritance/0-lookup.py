#!/usr/bin/python3
"""Module that defines a function to list attributes and methods"""


def lookup(obj):
    """Returns a list of available attributes and methods of an object"""
    return sorted(dir(obj))
