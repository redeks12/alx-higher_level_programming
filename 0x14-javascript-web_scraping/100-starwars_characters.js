#!/usr/bin/node

const request = require("request");
const id = process.argv[2];
const endpoint = `https://swapi-api.alx-tools.com/api/films/${id}`;

request({ url: endpoint, method: "GET", json: true }, (err, res, body) => {
  body.characters.forEach((item) => {
    request({ url: item, method: "GET", json: true }, (err, res, body) => {
      console.log(body.name);
    });
  });
});
