#!/usr/bin/python3
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        res = response.getheaders()
        print(res[0])
