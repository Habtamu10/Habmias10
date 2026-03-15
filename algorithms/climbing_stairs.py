# Climbing Stairs - LeetCode #70
def climb_stairs(n):
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

for i in range(1, 8):
    print(f"n={i}: {climb_stairs(i)} ways")
