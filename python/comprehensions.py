# Python Comprehensions
numbers = range(1, 11)

# List comprehension
squares = [n**2 for n in numbers]
evens = [n for n in numbers if n % 2 == 0]
pairs = [(x, y) for x in range(1, 4) for y in range(1, 4) if x != y]

# Dict comprehension
squared_dict = {n: n**2 for n in numbers}
filtered_dict = {k: v for k, v in squared_dict.items() if v > 25}

# Set comprehension
unique_remainders = {n % 3 for n in numbers}

# Generator expression
total = sum(n**2 for n in numbers)

print("Squares:", squares)
print("Evens:", evens)
print("Filtered dict:", filtered_dict)
print("Unique remainders mod 3:", unique_remainders)
print("Sum of squares:", total)
