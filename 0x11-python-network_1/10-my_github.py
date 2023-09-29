#!/usr/bin/python3
"""Write a Python script that fetches data"""
import sys

import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get(
        "https://api.github.com/users/{}".format(username),
        headers={"accept": "application/vnd.github+json"},
        auth=HTTPBasicAuth(username, password),
    )
    print(response.json())
    # print(response.json()["id"])
