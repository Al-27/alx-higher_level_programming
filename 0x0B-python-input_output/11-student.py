#!/usr/bin/python3
"""
    ...
    ...
"""

class Student:
    
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self, attrs=None):
        if attrs == None:
            return self.__dict__
        
        newDict = self.__dict__.copy()
        keyNot = []
        
        for key in newDict.keys():
            if not key in attrs:
                keyNot.append(key)
                
        for key in keyNot:
            newDict.pop(key)
            
        return newDict
    
    def reload_from_json(self, json):
        for key,val in json.items():
            self.__dict__[key] = val
