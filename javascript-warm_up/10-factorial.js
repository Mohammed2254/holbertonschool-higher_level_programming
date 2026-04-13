#!/usr/bin/node
const num = parseInt(process.argv[2]);

function factorial (num) {
  if (num <= 1 || isNaN(num)) {
    return (1);
  }

  return (factorial(num - 1) * num);
}
console.log(factorial(num));
