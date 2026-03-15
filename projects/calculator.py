# Simple Calculator
def add(a, b):      return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

def calculate(a, op, b):
    if op not in operations:
        raise ValueError(f"Unknown operator: {op}")
    return operations[op](a, b)

print(calculate(10, "+", 5))
print(calculate(10, "-", 3))
print(calculate(4, "*", 6))
print(calculate(15, "/", 3))
