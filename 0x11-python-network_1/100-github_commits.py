#!/usr/bin/python3
"""Write a Python script that fetches data"""
import sys

import requests

if __name__ == "__main__":
    response = requests.get(
        "https://api.github.com/repos/{}/{}/commits".format(sys.argv[2], sys.argv[1])
    )

    res = response.json()

    try:
        for resp in res[:10]:
            print(
                "{}: {}".format(
                    resp.get("sha"), resp.get("commit").get("author").get("name")
                )
            )
    except IndexError:
        pass
