#!/usr/bin/python3
"""Write a Python script that fetches data"""
import sys
from urllib import parse, request

if __name__ == "__main__":
    params = {"email": sys.argv[2]}
    data = parse.urlencode(params)
    data = data.encode("ascii")
    req = request.Request(sys.argv[1], data)
    with request.urlopen(req) as response:
        res = response.read()
        print(res.decode("utf8"))
