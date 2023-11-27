#!/usr/bin/python3
"""
    ...
    ...
"""

class MyInt(int):
    """
    ....
    """
    def __init__(self, i):
        super().__init__()
        
    def __eq__(self, other):
        return not (int(self) == other)
    
    def __ne__(self, i):
        return (int(self) == i)
