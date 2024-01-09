#!/usr/bin/node
if ( isNaN(process.argv[2])) {
  console.log('Missing size');
} 
else {
  const size = Number(process.argv[2]);
  let i = 0;
  while (i < x) {
    console.log('X'.repeat(size));
    i++;
  }
}

