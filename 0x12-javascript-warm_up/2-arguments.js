#!/usr/bin/node
const { argv } = require('process');

let count = argv.length - 2;

if( count == 0 ) console.log('No argument');
if( count == 1 ) console.log('Argument found');
else console.log('Arguments found');