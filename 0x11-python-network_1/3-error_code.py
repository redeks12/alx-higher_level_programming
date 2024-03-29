#!/usr/bin/python3
"""Write a Python script that fetches data"""
import sys
from urllib import error, request

if __name__ == "__main__":
    req = request.Request(sys.argv[1])
    try:
        with request.urlopen(req) as response:
            res = response.read()
            print(res.decode("utf-8"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
