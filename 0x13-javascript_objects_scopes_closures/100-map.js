#!/usr/bin/node
const list = require("./100-data").list;

let map = list.map(x => {
    let index = list.indexOf(x);
    return x * index; 
});

console.log(list);
console.log(map);