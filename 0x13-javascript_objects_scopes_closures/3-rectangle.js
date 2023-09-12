#!/usr/bin/node
module.exports = class Rectangle {
  constructor(w, h) {
    this.width = w;
    this.height = h;
  }

  print() {
    const x = "X".repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(x);
    }
  }
};
