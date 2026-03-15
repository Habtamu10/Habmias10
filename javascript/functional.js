// Functional Programming in JavaScript
const compose = (...fns) => x => fns.reduceRight((acc, fn) => fn(acc), x);
const pipe = (...fns) => x => fns.reduce((acc, fn) => fn(acc), x);

const curry = fn => {
    const arity = fn.length;
    return function curried(...args) {
        if (args.length >= arity) return fn(...args);
        return (...more) => curried(...args, ...more);
    };
};

const add = curry((a, b) => a + b);
const multiply = curry((a, b) => a * b);
const double = multiply(2);
const addTen = add(10);

const transform = pipe(double, addTen);
console.log([1, 2, 3, 4, 5].map(transform));

const words = ["hello", "world", "from", "JavaScript"];
const process = pipe(
    arr => arr.map(w => w.toUpperCase()),
    arr => arr.filter(w => w.length > 4),
    arr => arr.join(", ")
);
console.log(process(words));
