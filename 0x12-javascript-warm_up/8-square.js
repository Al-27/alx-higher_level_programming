#!/usr/bin/node
//const { argv } = require('process');

let size = parseInt( process.argv[2] );

if( isNaN(size) )
{
  console.log( 'Missing size' );
  size = 0;
}

let i = 0
while(i < size){
    console.log("X".repeat(size));
  i++;
}
