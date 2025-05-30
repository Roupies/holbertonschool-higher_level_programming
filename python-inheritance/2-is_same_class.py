def is_same_class(obj, a_class):
    """
    Check if obj is exactly an instance of a_class (no subclasses).

    Args:
        obj: any object
        a_class: class to check

    Returns:
        bool: True if obj is exactly instance of a_class, else False
    """
    return type(obj) is a_class
