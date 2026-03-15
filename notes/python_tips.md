# Python Tips and Best Practices

## List Comprehensions
```python
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
```

## Dict Comprehensions
```python
word_len = {word: len(word) for word in ["hello", "world"]}
```

## F-Strings (Python 3.6+)
```python
name = "Habtamu"
print(f"Hello, {name}!")
```

## Generators
```python
def gen_numbers(n):
    for i in range(n):
        yield i
```

## Useful Built-ins
```python
sorted(iterable, key=..., reverse=True)
enumerate(iterable, start=0)
zip(a, b)
map(func, iterable)
filter(func, iterable)
```
