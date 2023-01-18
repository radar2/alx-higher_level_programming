#!/usr/bin/node
// JS Script
require('request').get('https://swapi-api.alx-tools.com/api/films/' + process.argv[2] + '/', function (err, r, body) {
  if (err) {
    console.log(err);
  } else {	 
    console.log(JSON.parse(body).title);
  }
});
