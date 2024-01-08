#!/usr/bin/node
const { argv } = require('process');

let i = parseInt(argv[2]);

if( isNaN(i) ) console.log( 'Missing number of occurrences' );
else if ( i > 0 )
{
    for(let j = 0; j < i ; j++) console.log( 'C is fun' );
}