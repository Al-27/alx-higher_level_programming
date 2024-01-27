#!/usr/bin/python3
"""
Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris  
"""
from sys import argv
import urllib.request as request
import urllib.parse as prs
import urllib.error

try:
    with request.urlopen(argv[1]) as response:
        print( response.read().decode() )
except urllib.error.HTTPError as er :
    print(f"Error code: {er.code}")