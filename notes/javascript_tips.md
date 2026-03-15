# JavaScript Tips and Best Practices

## Destructuring
```javascript
const { name, age } = person;
const [first, ...rest] = array;
```

## Spread Operator
```javascript
const newArr = [...arr1, ...arr2];
const newObj = { ...obj1, extra: true };
```

## Optional Chaining
```javascript
const city = user?.address?.city;
```

## Nullish Coalescing
```javascript
const name = user.name ?? "Anonymous";
```

## Arrow Functions
```javascript
const add = (a, b) => a + b;
```

## Array Methods
```javascript
arr.map(fn)      // transform
arr.filter(fn)   // filter
arr.reduce(fn)   // accumulate
arr.find(fn)     // first match
arr.some(fn)     // any match
arr.every(fn)    // all match
```
