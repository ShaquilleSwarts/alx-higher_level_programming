#!/usr/bin/python3
# 8-rectangle.py
"""Define rectangle class"""


from curses.textpad import rectangle


class Rectangle:
    """represents a rectangle.

    Attributes:
            number_of_instances (int): Number of Instances
            Print_symbol (any): Symbol used for String representation.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Create new rectangle.

    arg:
        width(int): Width of rectangle
        height(int): height of rectangle
    """
        type(self).number_of_instances += 1
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
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return Rectangle with the greater area.
        Args:
            rect_1 : first Rectangle
            rect_2 : second Rectangle
        Raises:
            TypeError : if either args are not a Rectangle"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    def __str__(self):
        """return string representation.

        represents the rectangle with the # character"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return the string representation of the rectangle"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Print messages for the deletion of a rectangle"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
        
