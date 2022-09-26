#!/usr/bin/python3
# 3-is_kind_of_class.py
"""Defines class and inherited class-checking function """


def is_kind_of_class(obj, a_class):
    """Checks if Object is an instance of class or/and inherited class.

    args: obj (any): object to check
         a_class (any): the class to match
    Return :
        return True if class matches
        otherwise return False
    """
    if isinstance(obj, a_class):
        return True
    return False
