#!/usr/bin/python3
"""
hippity hoppity, this is a doc
"""
from sys import argv
import urllib.request as request

with request.urlopen(f'{argv[1]}') as response:
    print( response.headers["X-Request-Id"] )