# First steps wtih Kattis and Javascript

Here’s how to do basic Kattis tasks in Javascript, using the `Node.js` dialect.

## Environment

To begin use the online environment provided at `https://onecompiler.com/nodejs/`.
There is a simple editor in the left-hand pane, and you can write input in the North–East pane.
(Do avoid the online environment at `p5.js` – there is no way to provide input in that framework because it focusses on different libraries and a different run time environment.)

After solving dozens of Kattis tasks in this setting, you can consider installing a Javascript environment on your own machine.
Go to `node.js` for the runtime environment.
You also need an editor to write (and save) code on your machine.

## Input, Output, and Solutions

Most Kattis problems ask you to write a program that transforms input (say, `2 2`) to output (say, `4`). 

Output in javascript is printed using `console.log(string)`, so that’s easy.
Try to solve `hello`.


Input is a little bit trickier in Javascript and uses some advanced topics like event handlers.
Here’s a few lines of code that abstracts away all of these higher-order concepts and just puts all of input into an array of strings:

```javascript
const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, });
const input = []
rl.on('line', (line) => { input.push(line); });
rl.on('close', () => { solve(input) });

function solve(input) {
    // your code goes here
}
```

The input is now in the array of strings `input`.

### Kvedja

For instance, here is a solution to 
`open.kattis.com/problems/kvedja`:

```javascript
const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, });
const input = []
rl.on('line', (line) => { input.push(line); });
rl.on('close', () => { solve(input) });

function solve(input) {
    console.log("Kvedja,")
    console.log(input[0])
}
````

### Add Two Numbers

To solve `open.kattis.com/problems/addtwonumbers`, change the `solve` function to

```javascript
function solve(input) {
    let tokens = input[0].split(" ")
    let a = parseInt(tokens[0])
    let b = parseInt(tokens[1])
    console.log(a + b)
}
```

Note the conversion: `input[0]` (the first line of input) is a string of space-separated integers.
The `split(" ")`-function turns this into `tokens`, which has type `string[]` (“array of strings”).
The first element of that array `tokens[0]` is a string, say `"3"`.
The `parseInt` function turns that into an integer `3`.

### N-Sum

Here’s `nsum`:

```javascript
function solve(input) {
  let tokens = input[1].split(" ")
  let sum = 0;
  for (let i = 0; i < tokens.length; i++) {
    sum += parseInt(tokens[i], 10);
  }
  console.log(sum);
}
```


