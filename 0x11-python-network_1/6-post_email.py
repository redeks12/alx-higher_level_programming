#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    param = {"email": sys.argv[2]}
    response = requests.post(sys.argv[1], params=param)
    print(response.text)
