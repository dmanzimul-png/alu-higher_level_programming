#!/usr/bin/python3
"""Load object from JSON file"""

import json


def load_from_json_file(filename):
    """Read object from file"""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
