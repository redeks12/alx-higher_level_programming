#!/usr/bin/python3
"""Write a Python script that fetches data"""
import sys

import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    response = requests.get(
        "https://api.github.com/repos/{}/{}/commits".format(sys.argv[2], sys.argv[1])
    )
    res = response.json()
    for resp in res:
        print("{}: {}".format(resp["sha"], resp["commit"]["author"]["name"]))
