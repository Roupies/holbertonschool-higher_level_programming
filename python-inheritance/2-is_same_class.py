#!/usr/bin/python3

def is_same_class(obj, a_class):
    """Check if obj is exactly an instance of a_class (not a subclass)."""
    return type(obj) is a_class
