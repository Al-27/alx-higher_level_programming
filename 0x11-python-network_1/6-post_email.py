#!/usr/bin/python3
"""
hippity hoppity, this is a doc
"""
from sys import argv
import requests

if __name__ == "__main__":
    email = {"email" : argv[2]}
    post = requests.post(argv[1], data=email)

    print(post.text)