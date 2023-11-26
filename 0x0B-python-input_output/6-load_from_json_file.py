#!/usr/bin/python3
"""
    ...
"""
import json

def load_from_json_file(filename):
    """
        ...
    """
    str=""
    with open(filename, encoding='utf-8') as f:
        str = f.read()
    
    str = '[]' if str=="" else str 
    return json.loads(str)
        