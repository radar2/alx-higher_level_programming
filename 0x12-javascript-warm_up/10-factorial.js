#!/usr/bin/node
// JS

const num = parseInt(process.argv[2]);
console.log(factorial(num));

function factorial (n) {
  if (!n || n <= 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
