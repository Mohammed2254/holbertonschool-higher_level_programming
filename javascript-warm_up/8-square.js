#!/usr/bin/node
const arg = process.argv[2];
const times = parseInt(arg);
if (isNaN(times) === false) {
  for (let i = 0; i < times; i++) {
    let row = '';
    for (let j = 0; j < times; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
