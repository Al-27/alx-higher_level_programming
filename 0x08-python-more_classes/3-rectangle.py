#!/usr/bin/python3
"""Rectangle"""


class Rectangle:
    """Rectangle"""

    def __init__(self, w=0, h=0):
        self.check_valid(w, h)
        self.__width = w
        self.__height = h

    def width(self, value=None):
        if value is None:
            return self.__width

        if self.check_valid(w=value):
            self.__width = value

    def height(self, value=None):
        if value is None:
            return self.__height

        if self.check_valid(h=value):
            self.__height = value

    width = property(width, width)
    height = property(height, height)

    def check_valid(self, w=None, h=None):
        if w is not None:
            if isinstance(w, int):
                return True
            elif w < 0:
                raise ValueError("width must >= 0")
            else:
                raise TypeError("width must be an integer")
        if w is not None:
            if isinstance(h, int):
                return True
            elif h < 0:
                raise ValueError("height must >= 0")
            else:
                raise TypeError("height must be an integer")

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        w, h = self.__width, self.__height
        ret = ""
        if self.__width == 0 or self.__height == 0:
            return ret
        else:
            for i in range(h):
                ret += '#' * w + ("\n" if i + 1 < h else "")
        return ret
