# Counting Sort implementation
def counting_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    result = []
    for i, c in enumerate(count):
        result.extend([i] * c)
    return result

arr = [4, 2, 2, 8, 3, 3, 1]
print("Sorted:", counting_sort(arr))
