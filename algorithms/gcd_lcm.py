# GCD and LCM algorithms
from math import gcd

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def gcd_euclid(a, b):
    while b:
        a, b = b, a % b
    return a

pairs = [(12, 18), (7, 5), (100, 75)]
for a, b in pairs:
    print(f"GCD({a},{b}) = {gcd_euclid(a,b)}, LCM({a},{b}) = {lcm(a,b)}")
