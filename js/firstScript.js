// const fs = require('fs');

// const files = fs.readdirSync('./');

// console.log(files);


// const { log } = require('console');
const EventEmitter = require('events');

const emitter = new EventEmitter();

//Registor the Event

emitter.on('logging',(arg) =>{
    console.log('Listener Called', arg);
    
})

//event raise

emitter.emit('logging', {data : "Hello Bacho!!"})