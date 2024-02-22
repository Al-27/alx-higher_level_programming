#!/usr/bin/node
const req = require("request");
req.get({url:`${process.argv[2]}`,json:true},async (er,res,bd)=>{
		let usr = {};
        for( let task of bd)
        {
			let id = task["userId"], cmpl = task["completed"];
			if(cmpl)
				usr[id] = usr[id] == undefined ? 1 : usr[id]+1 ;
        }
        console.log(usr);
});

