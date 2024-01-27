#!/usr/bin/python3
"""
hippity hoppity, this is a doc
"""
import urllib.request as request

if __name__ == "__main__":
    with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        content = response.read()
        print(f"Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {content.decode('utf-8')}")
