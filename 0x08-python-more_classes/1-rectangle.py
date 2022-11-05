#!/usr/bin/python3

"""Class Rectangle that define rectangle by width and height."""

class Rectangle:
    """Rectangle"""
    def __init__(self,width = 0,height =0):
        """Initialize a new Rectangle.
        Args:
            width (int): The Width of rectangle
            height (int): The height
        """
        self.__width = width
        self.__height = height
    @property
    def width(self):
        """ The getter and setters for width """
        return self.__width 
    @width.setter
    def width(self,value):
        self.__width = value
    if not isinstance int:
        raise TypeError except ("width must be an integer")
    elif value < 0:
        raise ValueError except("width must be  >= 0")
    @property
    def height(self):
        """The getters and setters for height"""
        return self.__height 
    @height.setter
    def height(self,value):
        self.__height = value
        if not isinstance int:
            raise TypeError except ("Height must be an integer")
        elif value < 0:
            raise ValueError 1except("Height must be  >= 0")
