#!/usr/bin/python3
"""
hippity hoppity, this is a doc
"""
from sys import argv
import urllib.request as request
import urllib.parse as prs

if __name__ == "__main__":
    email = {"email": argv[2]}
    post = request.Request(argv[1], prs.urlencode(email).encode("utf-8"))

    with request.urlopen(post) as response:
        print(response.read().decode())
