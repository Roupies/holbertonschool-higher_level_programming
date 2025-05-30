#!/usr/bin/python3

def is_same_class(obj, a_class):

    """ Check if an object is exactly an instance of the given class.

    Parameters:
        obj: Any object to test.
        a_class: The class to compare with.

    Returns:
        bool: True if obj is an instance of exactly cls, else False.

    Example:
        is_same_class(obj, a_class)
        True
        is_same_class(obj, a_class)
        False
    """

    if type(obj) is a_class:
        return (True)
    else:
        return (False)
