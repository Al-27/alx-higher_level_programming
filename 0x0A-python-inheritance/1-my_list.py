#!/usr/bin/python3
"""
    ...
    ...
"""
class MyList(list):
    """
    ...
    """
    def print_sorted(self):
        list = self.copy()
        list.sort()
        print( list )
