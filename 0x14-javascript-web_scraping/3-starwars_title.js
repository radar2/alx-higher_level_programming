#!/usr/bin/node
// Script that prints the title of a Star Wars movie
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films';
require('request').get(`${url}/${id}`, function (err, res) {
  if (err) {
    console.log(err);
  } else {
    console.log(res.results[id].title);
  }
});
