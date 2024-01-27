#!/usr/bin/python3
"""
hippity hoppity, this is a doc
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