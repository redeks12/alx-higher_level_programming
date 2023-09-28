#!/bin/bash
# Bash script that takes in a URL, sends a request to it, and displays the size of the body of the response
curl sys.argv[1]
# size_i=$(echo $response | jq -r 'Content-length')