#!/usr/bin/node

const fs = require("fs");
const filename = process.argv[1];
const str = process.argv[2];

fs.writeFile(filename, str, "utf-8", (err) => {
  if (err) {
    console.log(err);
  }
});
