#!/usr/bin/node
const { argv } = require('process');

let i = parseInt(argv[2]);

if( isNaN(i) ) console.log( 'Not a number' );
else console.log( `My number: ${i}` );