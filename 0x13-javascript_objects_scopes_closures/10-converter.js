#!/usr/bin/node
// JS
exports.converter = function (base) {
  return function mainConvert (num) {
    return num.toString(base);
  };
};
