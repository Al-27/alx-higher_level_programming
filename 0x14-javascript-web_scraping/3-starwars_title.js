#!/usr/bin/node
const req = require("request");
req.get({url:`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`,json:true},async (er,res,bd)=>{
	console.log(er ? er :  bd["title"]);
});

