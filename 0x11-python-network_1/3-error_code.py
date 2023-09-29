#!/usr/bin/python3
import sys
from urllib import error, request

if __name__ == "__main__":
    req = request.Request(sys.argv[1])
    try:
        with request.urlopen(req) as response:
            res = response.read()
            print(res.decode("utf-8"))
    except error.HTTPError:
        print("Error code: {}", req.status)
