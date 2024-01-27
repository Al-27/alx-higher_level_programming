#!/usr/bin/node
class counter{
    count = -1;
    function () {;}
    cnt() {
        return ++this.count;        
    }
}
const ctr = new counter();
exports.logMe = function (item)
{ 
    console.log(`${ctr.cnt()}: ${item}`);    
}