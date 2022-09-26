#!/usr/bin/python3
# 9-rectangle.py
"""defines class"""


from curses.textpad import rectangle


class BaseGeometry():
    """Represents base geometry"""

    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Represents Rectangle based on BaseGeometry"""

    def __init__(self, width, height):
        """intialize a new Rectangle.

        Args:
            Width (int): The width of the new Rectangle
            Height (int): The height of the new Rectangle
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns the print() and str() representation of rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string


"""Defines a rectangle subclass Square"""


class Square(Rectangle):
    """Represents Square based on Rectangle"""

    def __init__(self, size):
        """intialize a new square

        Args:
            size (int) : The size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
