#!/usr/bin/python3

import json

__doc__ = """
Module: to_json_string

This module provides functionality to convert Python objects into JSON
string representations. It includes one main function:
- to_json_string: Converts a Python object to a JSON string

The module is part of a series of utility functions for handling JSON
data in Python.
"""


def to_json_string(my_obj):
    """
    Convert a Python object to a JSON string representation.

    Args:
        my_obj: The Python object to convert to JSON
            representation.

    Returns:
        str: A JSON string representation of the object.

    Raises:
        TypeError: If the object cannot be serialized to JSON.
    """
    return json.dumps(my_obj)
