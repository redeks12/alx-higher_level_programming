#!/usr/bin/node

const request = require("request");
const id = process.argv[2];
const endpoint = `https://swapi-api.alx-tools.com/api/films/${id}`;
let allUrls;

request({ url: endpoint, method: "GET", json: true }, (err, res, body) => {
  allUrls = body.characters;
});

setTimeout(() => {
  apicalls = function (urls, index) {
    if (index < urls.length) {
      request(
        { url: urls[index], method: "GET", json: true },
        (err, res, bd) => {
          console.log(bd.name);
        }
      );
      setTimeout(() => apicalls(urls, index + 1), 1000);
    }
  };
  apicalls(allUrls, 0);
}, 3000);
