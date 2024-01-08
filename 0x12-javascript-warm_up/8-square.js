#!/usr/bin/node
const { argv } = require('process');

let size = parseInt(argv[2]);

if( isNaN(size) ) console.log( 'Missing size' );
else if ( size > 0 )
{
    for(let i = 0; i < size ; i++) {
        let x = ""
        
        for(let j = 0; j < size; j++) x += "X";
        
        console.log(x);
    }
}