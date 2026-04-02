#!/usr/bin/python3
"""Save object to JSON file"""

import json


def save_to_json_file(my_obj, filename):
    """Write object to file"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
