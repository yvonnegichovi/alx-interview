#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <movieId>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch data (${response.statusCode}):`, body);
    process.exit(1);
  }

  try {
    const filmData = JSON.parse(body);
    const characters = filmData.characters;
    fetchAndPrintCharacters(characters);
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
    process.exit(1);
  }
});

function fetchAndPrintCharacters(characters) {
  characters.forEach((characterUrl) => {
    request.get(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error:', charError);
        return;
      }
      if (charResponse.statusCode === 200) {
        const characterData = JSON.parse(charBody);
        console.log(characterData.name);
      } else {
        console.error(`Failed to fetch character (${charResponse.statusCode}):`, charBody);
      }
    });
  });
}
