#!/usr/bin/node
// Handle arguments with Javascript
const myVar = process.argv[2];
if (myVar) {
  console.log(myVar);
} else {
  console.log("No argument");
}
