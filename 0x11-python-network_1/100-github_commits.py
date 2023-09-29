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
    try:
        for resp in res[:10]:
            print("{}: {}".format(resp["sha"], resp["commit"]["author"]["name"]))
    except IndexError:
        pass
