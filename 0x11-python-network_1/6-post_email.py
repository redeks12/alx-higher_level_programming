#!/usr/bin/python3
"""Write a Python script that fetches data"""
import sys

import requests

if __name__ == "__main__":
    param = {"email": sys.argv[2]}
    response = requests.post(sys.argv[1], data=param)
    print(response.text)
