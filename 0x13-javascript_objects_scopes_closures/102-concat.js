#!/usr/bin/node
const fs = require("fs");
let string = "";
for(let i = 2; i < 4; i++)
    string += fs.readFileSync(process.argv[i],"utf-8" ); 

fs.writeFileSync(process.argv[4], string);