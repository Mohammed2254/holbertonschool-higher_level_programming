#!/usr/bin/node
const len = process.argv.length;

if (len <= 3) {
  console.log(0);
} else {
  let i = 2;
  let j = 2;
  let biggest = Number(process.argv[i]);
  let biggestIndex = i;

  for (; i < len; i++) {
    if (biggest < Number(process.argv[i])) {
      biggest = Number(process.argv[i]);
      biggestIndex = i;
    }
  }

  let second = -Infinity;

  for (; j < len; j++) {
    if (j === biggestIndex) {
      continue;
    }
    if (second < Number(process.argv[j])) {
      second = Number(process.argv[j]);
    }
  }

  if (second === -Infinity) {
    console.log(0);
  } else {
    console.log(second);
  }
}
