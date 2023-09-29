#!/usr/bin/python3
import sys
from urllib import error, request

if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as respose:
            res = respose.read()
            print(res.decode("utf-8"))
    except error.HTTPError:
        print("Error code: {}", res.status_code)
