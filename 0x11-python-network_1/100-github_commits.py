#!/usr/bin/python3
"""
---
hippity hoppity, this is a doc
--DOCS
"""
import requests
import sys.argv
"""
---
hippity hoppity, this is a doc
--DOCS
"""
if __name__ == "__main__":
    """
    ---
    hippity hoppity, this is a doc
    --DOCS
    """
    headers = {"Accept": "application/vnd.github+json"}
    resp = requests.get(
        f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits?per_page=10",
        headers=headers)
    for js in resp.json():
        print(f'{js["sha"]}: {js["commit"]["author"]["name"]}')
