#!/usr/bin/python3
"""Convert JSON string to object"""

import json


def from_json_string(my_str):
    """Return Python object"""
    return json.loads(my_str)
