# Temperature Converter
def celsius_to_fahrenheit(c): return c * 9/5 + 32
def fahrenheit_to_celsius(f): return (f - 32) * 5/9
def celsius_to_kelvin(c):     return c + 273.15
def kelvin_to_celsius(k):     return k - 273.15

temps = [0, 20, 37, 100]
print(f"{'Celsius':>10} {'Fahrenheit':>12} {'Kelvin':>8}")
print("-" * 35)
for c in temps:
    print(f"{c:>10} {celsius_to_fahrenheit(c):>12.2f} {celsius_to_kelvin(c):>8.2f}")
