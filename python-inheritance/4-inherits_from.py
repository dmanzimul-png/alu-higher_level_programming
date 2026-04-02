#!/usr/bin/python3
"""Module that defines inherits_from function"""


def inherits_from(obj, a_class):
    """Returns True if object is subclass of a_class but not same"""
    return isinstance(obj, a_class) and type(obj) is not a_class
