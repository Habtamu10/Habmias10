# Python Generators
def infinite_counter(start=0, step=1):
    current = start
    while True:
        yield current
        current += step

def take(n, iterable):
    count = 0
    for item in iterable:
        if count >= n:
            break
        yield item
        count += 1

def fibonacci_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fibs = list(take(10, fibonacci_gen()))
print("Fibonacci:", fibs)

multiples = list(take(5, infinite_counter(3, 3)))
print("Multiples of 3:", multiples)
