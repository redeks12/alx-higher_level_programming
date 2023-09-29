#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    res = response.headers
    print(res.get("X-Request-Id"))
