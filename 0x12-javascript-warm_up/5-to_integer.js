#!/usr/bin/node
// Handle arguments with Javascript
const myVar = parseInt(process.argv[2]);
if (myVar) {
  console.log(`My number: ${myVar}`);
} else {
  console.log("Not a number");
}
