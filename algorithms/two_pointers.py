# Two Pointers technique
def two_sum_sorted(arr, target):
    """Find pair summing to target in sorted array"""
    left, right = 0, len(arr) - 1
    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            return [left, right]
        elif s < target:
            left += 1
        else:
            right -= 1
    return []

def remove_duplicates(arr):
    """Remove duplicates from sorted array in-place"""
    if not arr:
        return 0
    k = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            arr[k] = arr[i]
            k += 1
    return k

def container_with_most_water(heights):
    """Find max water container"""
    left, right = 0, len(heights) - 1
    max_water = 0
    while left < right:
        water = min(heights[left], heights[right]) * (right - left)
        max_water = max(max_water, water)
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return max_water

print(two_sum_sorted([1, 2, 3, 4, 6], 6))          # [1, 3]
print(container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
