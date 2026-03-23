#!/usr/bin/node
const size = parseInt(process.argv[2]);

if (Number.isNaN(size)) {
  console.log('Missing size');
} else {
  for (let index = 0; index < size; index++) {
    console.log('X'.repeat(size));
  }
}
