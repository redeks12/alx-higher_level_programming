#!/usr/bin/node

const request = require("request");
const endpoint = process.argv[2];

request(endpoint, (err, header) => {
  if (err) {
    console.log(err);
  } else {
    console.log(`code: ${header.statusCode}`);
  }
});
