#!/usr/bin/python3
"""
    ...
    ...
"""
class BaseGeometry:
    
    def area(self):
        if self.__getattribute__("area"):        
            raise Exception("area() is not implemented")


bg = BaseGeometry()