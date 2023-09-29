#!/usr/bin/python3
import sys

import requests

if __name__ == "__main__":
    try:
        param = {"q": sys.argv[1]}
    except IndexError:
        param = {"q": ""}
    response = requests.post("http://0.0.0.0:5000/search_user", data=param)
    res = response.json()
    print(res)
    print(response.text)
    try:
        if res:
            print("[{}] {}".format(res["id"], res["name"]))
        else:
            print("No result")
    except requests.JSONDecodeError:
        print("Not a valid JSON")
