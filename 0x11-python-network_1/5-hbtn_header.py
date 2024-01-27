#!/usr/bin/python3
"""
hippity hoppity, this is a doc
"""
from sys import argv
import requests

if __name__ == "__main__":
    with requests.get(f'{argv[1]}') as response:
        print(response.headers["X-Request-Id"])
