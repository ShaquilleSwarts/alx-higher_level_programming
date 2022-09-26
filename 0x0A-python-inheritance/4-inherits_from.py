#!/usr/bin/python3
# 4-inherits_from.py
"""Defines a inherited class-checking function"""


def inherits_from(obj, a_class):
    """Checks if object is an instance of inherited class.

    Args:
        Obj (any): Object being checked
        a_class (any): class to match
    Returns:
        Return True if object is a instance of inherited class
        Otherwise Return False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
