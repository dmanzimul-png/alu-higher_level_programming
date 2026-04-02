#!/usr/bin/python3
"""0-lookup.py"""

def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.
    Args:
        obj (any): The object to inspect.
    Returns:
        list: List of attribute and method names.
    """
    return dir(obj)
