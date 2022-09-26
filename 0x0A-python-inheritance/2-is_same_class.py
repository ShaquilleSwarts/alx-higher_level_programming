#!/usr/bin/python3
# 2-is_same-class.py
"""checks class-defining function"""

def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of given class.

    args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class -True.
        otherwise -False
        """
    if type(obj) == a_class:
        return True
    return False
