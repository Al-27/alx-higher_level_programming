#!/usr/bin/python3
"""
---
hippity hoppity, this is a doc
--DOCS
"""
import requests
import sys

if __name__ == "__main__":

    headers = {"Accept": "application/vnd.github+json"}
    resp = requests.get(
        f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits?per_page=10",
        headers=headers)
    for js in resp.json():
        print(f'{js["sha"]}: {js["commit"]["author"]["name"]}')
