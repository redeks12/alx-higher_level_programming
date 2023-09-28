#!/bin/bash
# Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -X POST -s -d "email=test@gmail.com&subject=I will always be here for PLD" $1
