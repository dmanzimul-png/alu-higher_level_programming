#!/usr/bin/python3
"""Return dictionary description of object"""


def class_to_json(obj):
    """Return dictionary"""
    return obj.__dict__
