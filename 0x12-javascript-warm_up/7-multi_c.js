#!/usr/bin/node
// JS

const len = parseInt(process.argv[2]);
if (len) {
  for (let i = 0; i < len; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
