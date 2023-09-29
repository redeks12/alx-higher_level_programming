#!/usr/bin/python3
import sys

import requests

if __name__ == "__main__":
    try:
        param = {"q": sys.argv[1]}
    except IndexError:
        param = {"q": ""}
    response = requests.post("http://0.0.0.0:5000/search_user", params=param)
    res = response.json()
    print(res)
    try:
        if res:
            print("[{}] {}".format(res["id"], res["name"]))
        else:
            print("No result")
    except requests.JSONDecodeError:
        print("Not a valid JSON")
