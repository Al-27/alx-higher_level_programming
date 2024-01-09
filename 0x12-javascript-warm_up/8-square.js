#!/usr/bin/node
  let size = parseInt(process.argv[2]);
if ( isNaN(process.argv[2])) {
  console.log('Missing size');
} 
else {
  let i = 0;
  while (i < size) {
    console.log('X'.repeat(size));
    i++;
  }
}

