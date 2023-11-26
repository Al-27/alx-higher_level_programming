#!/usr/bin/python3
"""
    ...
    ...
"""
from sys import argv 
from os import path
save = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file").load_from_json_file
if __name__ == "__main__":
    """
        ...
        ...
    """
    fname = "add_item.json"
    if path.isfile(fname) == False:
        f = open(fname, "w")
        f.close()
    
    obj = load(fname)
    obj += argv[1:] 
    save(obj,fname)
