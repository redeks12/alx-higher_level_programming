#!/usr/bin/node

const request = require("request");
const fs = require("fs");
const endpoint = process.argv[2];
const filename = process.argv[3];

request({ url: endpoint, method: "GET" }, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(filename, body, "utf8", (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
