#!/usr/bin/node
const { argv } = require('process');

let num = parseInt(argv[2]) ;

if( isNaN(num) ) console.log( '1' );
else
{
    let sum = fact( num );
    
    console.log(sum);
}

function fact(a)
{
    let sum = 1;
    if( a > 1 ) sum *= fact( a-1 );
    
    return a * sum ;
}
