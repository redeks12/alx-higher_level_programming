#!/usr/bin/node

const request = require("request");
const id = process.argv[2];
const endpoint = `https://swapi-api.alx-tools.com/api/films/${id}`;

request({ url: endpoint, method: "GET", json: true }, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log(body.title);
  }
});
