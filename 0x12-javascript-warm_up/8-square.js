#!/usr/bin/node
//const { argv } = require('process');


if( process.argv[2] === undefined || isNaN(process.argv[2]) ) console.log( 'Missing size' );
else
{
let size = parseInt( process.argv[2] );
  let i = 0
    while(i < size){
        console.log("X".repeat(size));
      i++;
    }
}
