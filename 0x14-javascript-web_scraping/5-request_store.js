#!/usr/bin/node

const proc = require("process");
const fs = require("fs");
const req = require("request");
req(proc.argv[2], (e, r, b) =>{
	if(!e)
		fs.writeFile(proc.argv[3],b,"utf8", er => {
			if(er)	console.log(er);
		});
});

