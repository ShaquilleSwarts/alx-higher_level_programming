#!/usr/bin/python3
# 2-rectangle.py
"""Define rectangle class"""


class Rectangle:
    """represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Create new rectangle.

    arg:
        width(int): Width of rectangle
        height(int): height of rectangle
    """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns Perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2)+(self.__height * 2))
