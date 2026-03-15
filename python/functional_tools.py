# Python Functional Tools: map, filter, reduce
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

doubled   = list(map(lambda x: x * 2, numbers))
evens     = list(filter(lambda x: x % 2 == 0, numbers))
total     = reduce(lambda acc, x: acc + x, numbers)
product   = reduce(lambda acc, x: acc * x, numbers)

print("Doubled:", doubled)
print("Evens:", evens)
print("Sum:", total)
print("Product:", product)

# Chaining operations with pipe-like style
pipeline = lambda data: reduce(
    lambda acc, fn: fn(acc),
    [
        lambda x: filter(lambda n: n % 2 == 0, x),
        lambda x: map(lambda n: n ** 2, x),
        list,
    ],
    data
)
print("Even squares:", pipeline(numbers))
