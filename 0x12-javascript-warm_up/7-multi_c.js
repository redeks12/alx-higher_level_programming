#!/usr/bin/node
// Handle arguments with Javascript
if (process.argv.length >= 3) {
  const myVar = parseInt(process.argv[2]);
  for (let index = 0; index < myVar; index++) {
    console.log("C is fun");
  }
} else {
  console.log("Missing number of occurrences");
}
