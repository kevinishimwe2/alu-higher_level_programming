#!/usr/bin/node
const { argv } = require('process');
argv.forEach((arg, index) => {
  if (index === 0) {
    console.log('Argument 0: ' + arg);
  } else if (index === 1) {
    console.log('Argument 1: ' + arg);
  }
});
