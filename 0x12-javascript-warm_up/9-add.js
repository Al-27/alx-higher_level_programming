#!/usr/bin/node
const { argv } = require('process');

let num1 = parseInt(argv[2]) , num2 = parseInt(argv[3]) ;

if( isNaN(num1) || isNaN(num2) ) console.log( 'NaN' );
else
{
    let sum = add( num1, num2);
    
    console.log(sum);
}

function add(a, b)
{
    return a + b;
}