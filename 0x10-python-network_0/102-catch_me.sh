#!/bin/bash
# Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s -L -X PUT -H "Origin: HolbertonSchool" -d 'user_id=98' 0.0.0.0:5000/catch_me
