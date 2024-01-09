#!/usr/bin/node
//const { argv } = require('process');

let size = parseInt( process.argv[2] );

if( process.argv[2] === undefined || isNaN(size) ) console.log( 'Missing size' );
else
{
  let i = 0
    while(i < size){
        console.log("X".repeat(size));
      i++;
    }
}
