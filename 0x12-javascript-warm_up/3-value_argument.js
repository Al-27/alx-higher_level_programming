#!/usr/bin/node
const { argv } = require('process');

if( argv[2] == undefined ) console.log('No argument');
else argv.forEach((v,i) => {
    if(i > 1) console.log(v);
});
