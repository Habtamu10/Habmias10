// JavaScript Closures
function makeCounter(start = 0) {
    let count = start;
    return {
        increment: () => ++count,
        decrement: () => --count,
        value: () => count,
        reset: () => { count = start; }
    };
}
const counter = makeCounter(10);
console.log(counter.increment()); // 11
console.log(counter.increment()); // 12
console.log(counter.decrement()); // 11
console.log(counter.value());     // 11
counter.reset();
console.log(counter.value());     // 10
