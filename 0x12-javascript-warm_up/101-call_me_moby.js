#!/usr/bin/node
exports.callMeMoby = function (iter, callback)
{
    for(let i = 0; i < iter; i++) callback();
}