#!/usr/bin/node
exports.converter = function (base) {
  return function con(num) {
    return num.toString(base);
  };
};
