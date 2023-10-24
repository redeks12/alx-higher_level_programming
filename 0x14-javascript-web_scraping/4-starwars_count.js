#!/usr/bin/node

const request = require("request");
const id = 18;
const endpoint = process.argv[2];
let num = 0;

request({ url: endpoint, method: "GET", json: true }, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    for (let i = 0; i < body.results.length; i++) {
      body.results[i].characters.forEach((item) => {
        if (item === `https://swapi-api.alx-tools.com/api/people/${id}/`) {
          num++;
        }
      });
    }
    console.log(num);
  }
});
