#!/usr/bin/node
exports.nbOccurences = function (list, searchElement){
    let occ = 0;
    
    list.forEach(element => {
        if (element == searchElement)
        {
            occ++;
        }
    });
    
    return occ;
}