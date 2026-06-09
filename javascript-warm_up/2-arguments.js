#!/usr/bin/node
const argv = process.argv.slice(2);
argv.forEach((arg, index) => {
  if (index === 0) {
    console.log('No argument');
  } else if (index === 1) {
    console.log('Argument found');
  }
  else {
    console.log('Arguments found');
  }
});
