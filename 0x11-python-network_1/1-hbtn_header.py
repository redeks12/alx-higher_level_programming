#!/usr/bin/python3
"""Write a Python script that fetches data"""
import sys
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        res = dict(response.getheaders())
        print(res.get("X-Request-Id"))
