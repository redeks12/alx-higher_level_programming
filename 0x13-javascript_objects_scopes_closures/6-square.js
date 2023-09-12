#!/usr/bin/node

module.exports = class Square extends require("./5-square") {
  charPrint(c) {
    let x;
    if (c) {
      x = c;
    } else {
      x = "X";
    }
    x = x.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(c);
    }
  }
};
