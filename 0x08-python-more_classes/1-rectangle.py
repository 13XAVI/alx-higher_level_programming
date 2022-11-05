#!/bin/python3

"""Class Rectangle that define rectangle by width and height."""

class Rectangle:
    """initialization and add property"""
    def __init__(self,width = 0,height =0):
        self.__width = width
        self.__height = height
    @property
    def width(self):
        self.__width = width
    @setter.width
    def width(self,value):
        self.__width = value
    if not isinstance int:
        raise TypeError except ("width must be an integer")
    elif(value < 0):
        raise ValueError except("width must be  >= 0")
    @property
    def height(self):
        self.__height = height
    @setter.height
    def height(self,value):
        self.__height = value
        if not isinstance int:
            raise TypeError except ("Height must be an integer")
        elif(value < 0):
            raise ValueError except("Height must be  >= 0")

