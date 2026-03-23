#!/usr/bin/node
const numbers = process.argv.slice(2).map(Number);

if (numbers.length < 2) {
  console.log(0);
} else {
  let biggest = numbers[0];
  let secondBiggest = -Infinity;

  for (let index = 1; index < numbers.length; index++) {
    if (numbers[index] > biggest) {
      secondBiggest = biggest;
      biggest = numbers[index];
    } else if (numbers[index] > secondBiggest && numbers[index] !== biggest) {
      secondBiggest = numbers[index];
    }
  }

  console.log(secondBiggest === -Infinity ? 0 : secondBiggest);
}
