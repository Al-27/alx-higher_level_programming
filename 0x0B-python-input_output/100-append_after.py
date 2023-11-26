#!/usr/bin/python3
"""
    ...
    ...
"""

def append_after(filename="", search_string="", new_string=""):
    """
    ...
    """
    newTxt = ""
    with open("text","r+") as file:
        for line in file:
            newTxt += line
            if search_string in line:
                newTxt += new_string
    
    with open("text","w") as file: 
        file.write(newTxt)
