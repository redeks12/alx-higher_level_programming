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

  rotate() {
    let h = this.height;
    this.height = this.width;
    this.width = h;
  }

  double() {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
