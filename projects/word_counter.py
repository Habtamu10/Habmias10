# Word Frequency Counter
from collections import Counter
import re

def word_frequency(text):
    words = re.findall(r"\b[a-z]+\b", text.lower())
    return Counter(words)

text = """
Python is a high-level programming language.
Python is easy to learn and Python is powerful.
Programming with Python is fun and rewarding.
"""

freq = word_frequency(text)
print("Top 5 words:")
for word, count in freq.most_common(5):
    print(f"  {word}: {count}")
