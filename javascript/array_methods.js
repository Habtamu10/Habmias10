// JavaScript Array Methods
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const evens = numbers.filter(n => n % 2 === 0);
const squares = numbers.map(n => n * n);
const sum = numbers.reduce((acc, n) => acc + n, 0);
const found = numbers.find(n => n > 5);
console.log("Evens:", evens);
console.log("Squares:", squares);
console.log("Sum:", sum);
console.log("First > 5:", found);
