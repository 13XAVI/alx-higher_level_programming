#!/usr/bin/python3

"""Class Rectangle that define a rectangle by width and height."""

class Rectangle:
    """Rectangle"""
    def __init__(self,width=0, height =0):
        """Initialize a new Rectangle.
        Args:
            width (int): The Width of rectangle
            height (int): The height
        """
        self.width = width
        self.height = height
    @property
    def width(self):
        """ The getter and setters for width """
        return self.__width 
    @width.setter
    def width(self, value):
        if not isinstance (value, int):
        raise TypeError("width must be an integer")
        elif value < 0:
        raise ValueError("width must be  >= 0")
        self.__width = value
    @property
    def height(self):
        """The getters and setters for height"""
        return self.__height 
    @height.setter
    def height(self,value):
        if not isinstance (value, int):
            raise TypeError("Height must be an integer")
        elif value < 0:
            raise ValueError("Height must be  >= 0")
        self.__height = value
