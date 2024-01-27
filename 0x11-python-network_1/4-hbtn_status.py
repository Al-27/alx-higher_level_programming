#!/usr/bin/python3
"""
hippity hoppity, this is a doc
"""
import urllib.request as request

with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    content = response.read()
    print(f"""Body response:$
    - type: {type(content.decode())}$
    - utf8 content: {content.decode()}$""")