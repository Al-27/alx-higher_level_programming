#!/usr/bin/node
//const list = require("./100-data").dict;
let list = [1,8,3,9,99,9];

let map = list.map(x => {
    let index = list.indexOf(x);
    return index == 0 ? 0 : x * list[index-1]; 
});

console.log(list);
console.log(map);