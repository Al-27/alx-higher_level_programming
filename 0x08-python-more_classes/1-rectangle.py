#!/usr/bin/python3
"""Rectangle"""
class Rectangle:
    """Rectangle"""
    def __init__(self, w=0, h=0):
        self.__width = self.width(w)
        self.__height = self.height ( h)
    
    def width(self, value=None):
        if value == None:
            return self.__width
         
        if isinstance(value,int) :
            self.__width = value
        elif value < 0 :
            raise ValueError("width must >= 0")
        else:
            raise TypeError("width must be an integer")
            
    def height(self, value=None):
        if value == None:
            return self.__height
        
        if isinstance(value,int):
            self.__height = value 
            return value
        elif value < 0 :
            raise ValueError("height must >= 0")
        else:
            raise TypeError("height must be an integer")
                 
        
