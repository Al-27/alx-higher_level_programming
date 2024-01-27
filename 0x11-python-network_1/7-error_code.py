#!/usr/bin/python3
"""
hippity hoppity, this is a doc
"""
from sys import argv
import requests


if __name__ == "__main__":
    response = requests.get(argv[1])

    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Error code: {response.status_code}")
