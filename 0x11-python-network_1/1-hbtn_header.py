#!/usr/bin/python3
"""
Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris  
"""
from sys import argv
import urllib.request as request

if __name__ == "__main__":
    with request.urlopen(f'{argv[1]}') as response:
        print( response.headers["X-Request-Id"] )