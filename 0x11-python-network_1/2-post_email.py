#!/usr/bin/python3
"""
Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris  
"""
from sys import argv
import urllib.request as request
import urllib.parse as prs

email = {"email" : argv[2]}
post = request.Request(argv[1], prs.urlencode(email).encode("utf-8"))


with request.urlopen(post) as response:
    print( response.read().decode() )