#!/usr/bin/python3
"""
hippity hoppity, this is a doc
"""
import urllib.request as request

if __name__ == "__main__":
    with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        content = response.read()
        print(f"""Body response:$
        - type: {type(content)}$
        - content: {content}$
        - utf8 content: {content.decode('utf-8')}$""")