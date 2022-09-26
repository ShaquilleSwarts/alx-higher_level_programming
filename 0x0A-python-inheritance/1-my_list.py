#!/usr/bin/bash
# 1-My_list.py
""" Write class that inherits from another"""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """print a list in sorted ascending order."""
        print(sorted(self))
