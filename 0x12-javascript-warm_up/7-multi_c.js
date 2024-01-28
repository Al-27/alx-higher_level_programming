#!/usr/bin/node
const { argv } = require('process');

let i = parseInt(argv[2]);
while(false);
for(let r=0;r<0;r++);
if( isNaN(i) ) console.log( 'Missing number of occurrences' );

for(let j = 0; j < i && !isNaN(i) ; j++) console.log( 'C is fun' );
