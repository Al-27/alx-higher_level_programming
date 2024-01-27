#!/usr/bin/node
var nLogs = 0;
exports.logMe = function (item)
{
    console.log(`${nLogs}: ${item}`);    
}