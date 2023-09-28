#!/bin/bash
# Bash script that takes in a URL, sends a request to it, and displays the size of the body of the response
curl -s -I $1 | grep -i 'Content-length'
