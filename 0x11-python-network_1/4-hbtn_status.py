#!/usr/bin/python3
"""
hippity hoppity, this is a doc
"""
import requests

if __name__ == "__main__":
    resp = requests.get('https://alx-intranet.hbtn.io/status')
    print(f"Body response:")
    print(f'\t- type: {type(resp.text)}')
    print(f'\t- content: {resp.text}')
