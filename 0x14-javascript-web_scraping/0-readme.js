#!/usr/bin/node
const proc = require("process");
const fs = require("fs");
fs.readFile(proc.argv[2],"utf8",(er,data)=>{
	if(er)	console.log(er);
	else	console.log(data);
});

