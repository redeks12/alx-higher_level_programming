#!/usr/bin/node

const request = require("request");
const endpoint = process.argv[2];
let bas = {};

request({ url: endpoint, method: "GET", json: true }, (err, res, body) => {
  body.forEach((item) => {
    bas[item.userId] = 0;
  });
  Object.keys(bas).forEach((key) => {
    console.log(key);
    body.forEach((item) => {
      if (key == item.userId && item.completed === true) {
        bas[item.userId]++;
      }
    });
  });

  Object.keys(bas).forEach((key) => {
    if (bas[key] === 0) {
      delete bas[key];
    }
  });

  console.log(bas);
});
