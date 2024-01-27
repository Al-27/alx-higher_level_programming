#!/usr/bin/python3

from sys import argv
import urllib.request as request

"""
Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris  
"""

with request.urlopen(f'{argv[1]}') as response:
    print( response.headers["X-Request-Id"] )