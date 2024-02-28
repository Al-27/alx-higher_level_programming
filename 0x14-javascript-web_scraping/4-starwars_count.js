#!/usr/bin/node
const req = require("request");
req.get({url: process.argv[2], json:true}, (er, res, bd) => {

	console.log( er ? er : JSON.stringify(bd).match(/people\/18\//g).length);});

