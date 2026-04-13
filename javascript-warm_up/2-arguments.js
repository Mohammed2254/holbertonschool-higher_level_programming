#!/usr/bin/node
const first = process.argv[2];

if (first) {
  const second = process.argv[3];
  if (second) {
    console.log('Arguments found');
  } else {
    console.log('Argument found');
  }
} else {
  console.log('No argument');
}
