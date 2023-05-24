#!/usr/bin/node
// Script that reads and prints the content of a file.
const fs = require('fs');
fs.readFile(process.argv[2], function (err, data) {
  if (!err) {
    console.log(data.toString().trim());
  } else {
    console.log(err);
  }
});
