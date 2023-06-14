<<<<<<< HEAD
#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;
request(url, async function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      const res = await new Promise((resolve, reject) => {
        request(character, (error, res, html) => {
          if (error) {
            reject(error);
          } else {
            resolve(JSON.parse(html).name);
          }
        });
      });
      console.log(res);
    }
  }
});
=======
#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(url, async (err, res, body) => {
  err && console.log(err);

  const charactersArray = (JSON.parse(res.body).characters);
  for (const character of charactersArray) {
    await new Promise((resolve, reject) => {
      request(character, (err, res, body) => {
        err && console.log(err);

        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});


>>>>>>> 38010625026043076017e745a50d0e0e7a750eb5
