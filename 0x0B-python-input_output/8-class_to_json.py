#!/usr/bin/python3
"""
    ...
    ...
"""

def class_to_json(obj):
    """
        ...
    """
    if obj == None:
        return "{}"
    
    return  obj.__dict__ 