#!/usr/bin/python3
"""
    ...
    ...
"""

def append_after(filename="", search_string="", new_string=""):
    """
    ...
    """
    
    with open(filename,"r+") as file:
        newTxt = ""
        for line in file:
            newTxt += line
            if search_string in line:
                newTxt += new_string
        file.seek(0,0)
        file.write(newTxt)
