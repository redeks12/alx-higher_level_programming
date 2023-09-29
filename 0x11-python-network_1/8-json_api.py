#!/usr/bin/python3
"""Write a Python script that fetches data"""
import sys

import requests

if __name__ == "__main__":
    try:
        param = {"q": sys.argv[1]}
    except IndexError:
        param = {"q": ""}
    response = requests.post("http://0.0.0.0:5000/search_user", data=param)
    res = response.json()
    try:
        if res:
            print("[{}] {}".format(res.get("id"), res.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
