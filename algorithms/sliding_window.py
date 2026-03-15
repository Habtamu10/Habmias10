# Sliding Window technique
def max_sum_subarray(arr, k):
    """Find max sum of subarray of size k"""
    n = len(arr)
    if n < k:
        return None
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, n):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum

def longest_substring_no_repeat(s):
    """Longest substring without repeating characters"""
    char_index = {}
    max_len = start = 0
    for end, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        char_index[char] = end
        max_len = max(max_len, end - start + 1)
    return max_len

arr = [2, 1, 5, 1, 3, 2]
print("Max sum of size 3:", max_sum_subarray(arr, 3))  # 9
print("Longest no-repeat 'abcabcbb':", longest_substring_no_repeat("abcabcbb"))  # 3
