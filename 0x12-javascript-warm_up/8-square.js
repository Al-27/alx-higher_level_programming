#!/usr/bin/node
//const { argv } = require('process');

let size = parseInt( process.argv[2] );
let tmp = size;
if( isNaN(size) ) console.log( 'Missing size' );
else
{
    while(tmp--) {
        console.log("X".repeat(size));
    }
}
