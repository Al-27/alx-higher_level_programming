#!/usr/bin/python3
"""
Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris  
"""
import urllib.request as request

with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    content = response.read()
    print(f"""Body response:$
    - type: {type(content)}$
    - content: {content}$
    - utf8 content: {content.decode('utf-8')}$""")