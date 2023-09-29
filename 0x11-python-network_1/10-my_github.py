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
            "X-GitHub-Api-Version": "2022 - 11 - 28",
        },
    )
    # print(response.json()["id"])
    print(response.json())
