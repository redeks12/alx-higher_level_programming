#!/usr/bin/python3
"""Write a Python script that fetches data"""
import sys

import requests

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    res = response.headers
    print(res.get("X-Request-Id"))
