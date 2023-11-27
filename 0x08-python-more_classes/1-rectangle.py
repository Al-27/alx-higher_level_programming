#!/usr/bin/python3
"""Rectangle"""
class Rectangle:
    """Rectangle"""
    def __init__(self, w=0, h=0):
        self.check_valid(w,h)
        self.__width = w
        self.__height = h
    
    
    def width(self, value=None):
        if value == None:
            return self.__width
         
        if self.check_valid(w=value):
            self.__width = value
            
    def height(self, value=None):
        if value == None:
            return self.__height
        
        if self.check_valid(h=value):
            self.__height = value 
    
    
    width = property(width,width)
    height = property(height,height)
    
    def check_valid(self, w=None, h=None):
        mustbe = " must >= 0"
        mustbe2 = " must be an integer"
        
        if w != None:
            if isinstance(w,int) : 
                if w < 0 :
                    raise ValueError("width" + mustbe)
            else:
                raise TypeError("width" + mustbe2)                
        if h != None:
            if isinstance(h,int):
                if h < 0 :
                    raise ValueError("height" + mustbe)
            else:
                raise TypeError("height" + mustbe2)
        return True