#!/usr/bin/python3
from urllib import request, parse
import sys

if __name__ == "__main__":
    params = {"email": sys.argv[2]}
    data = parse.urlencode(params)
    req = request.Request(sys.argv[1], data)
    with request.urlopen(req) as response:
        res = response.read()
        print(res.decode("utf8"))
