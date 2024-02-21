#!/usr/bin/node

const proc = require("process");
const fs = require("fs");
fs.writeFile(proc.argv[2],proc.argv[3],"utf8", er => {
	if(er)	console.log(er);
});

