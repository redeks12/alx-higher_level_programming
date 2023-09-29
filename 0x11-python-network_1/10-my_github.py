#!/usr/bin/python3
"""Write a Python script that fetches data"""
import sys

import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get(
        "https://api.github.com/user",
        auth=HTTPBasicAuth(username, password),
    )
    res = response.json()
    print(res.get("id"))
