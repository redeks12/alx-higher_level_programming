#!/usr/bin/python3
"""Write a Python script that fetches data"""
import sys

import requests

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get(
        "https://api.github.com/users/{}".format(username),
        headers={
            "Authorization": "token {}".format(password),
            "Accept": "application/vnd.github.v3+json",
        },
    )
    # print(response.json()["id"])
    print(response.json())
