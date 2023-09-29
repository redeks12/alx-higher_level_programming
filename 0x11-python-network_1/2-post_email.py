#!/usr/bin/python3
import urllib.request
import sys

if __name__ == "__main__":
    params = {"email": sys.argv[2]}
    url = "{}?{}".format(sys.argv[1], params)
    with urllib.request.urlopen(url) as response:
        res = response.read()
        print(res.decode("utf8"))
