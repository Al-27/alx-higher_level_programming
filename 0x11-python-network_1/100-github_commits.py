#!/usr/bin/python3
"""
hippity hoppity, this is a doc
"""
import requests

if __name__ == "__main__":
    headers = {"Accept": "application/vnd.github+json"}
    resp = requests.get(
        "https://api.github.com/repos/rails/rails/commits?per_page=10",
        headers=headers)
    for js in resp.json():
        print(f'{js["sha"]}: {js["commit"]["author"]["name"]}')
