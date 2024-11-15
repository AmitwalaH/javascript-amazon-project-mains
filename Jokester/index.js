const jokes = require('give-me-a-joke');
const punycode = require('punycode');
const colors = require('colors');
jokes.getRandomDadJoke(function (joke){
    console.log(joke.rainbow);    
})