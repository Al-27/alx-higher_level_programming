#!/usr/bin/node
const req = require("request");
req.get({url:`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`,json:true},async (er,res,bd)=>{
	let chars = bd["characters"];
	for( let c of chars)
	{
		let ch = await new Promise((resp,rej)=>{req.get({url:c,json:true},(er,res,bd)=>resp(bd["name"]))});
		console.log(ch);
	}
});

