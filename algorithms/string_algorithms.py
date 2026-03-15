# Common String Algorithms
from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1.lower()) == Counter(s2.lower())

def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
        if not prefix:
            return ""
    return prefix

def reverse_words(sentence):
    return " ".join(sentence.split()[::-1])

print(is_anagram("listen", "silent"))
print(longest_common_prefix(["flower", "flow", "flight"]))
print(reverse_words("Hello World from Python"))
