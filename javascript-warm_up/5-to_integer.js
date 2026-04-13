#!/usr/bin/node
const arg = process.argv[2];
const myInt = parseInt(arg);

if (isNaN(myInt)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + myInt);
}
