#!/usr/bin/node
// Script that display the status code of a GET request.
require('request').get(process.argv[2], function (err, res) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + res.statusCode);
  }
});
