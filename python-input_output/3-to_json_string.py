#!/usr/bin/python3

import json

"""
Module that contains the function to_json_string
"""

def to_json_string(my_obj):
    """
    Convert a Python object to a JSON string representation.

    Args:
        my_obj: The Python object to convert to JSON.

    Returns:
        str: A JSON string representation of the object.

    Raises:
        TypeError: If the object cannot be serialized to JSON.
    """
    return json.dumps(my_obj)
