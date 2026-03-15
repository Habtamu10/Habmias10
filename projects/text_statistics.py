# Text Statistics Analyzer
def analyze_text(text):
    lines = text.strip().split("\n")
    words = text.split()
    chars = len(text)
    chars_no_space = len(text.replace(" ", "").replace("\n", ""))
    sentences = text.count(".") + text.count("!") + text.count("?")
    print(f"Lines:            {len(lines)}")
    print(f"Words:            {len(words)}")
    print(f"Characters:       {chars}")
    print(f"Chars (no space): {chars_no_space}")
    print(f"Sentences:        {sentences}")
    if len(words) > 0:
        print(f"Avg word length:  {chars_no_space / len(words):.2f}")

sample = """
Python is a versatile programming language.
It supports multiple programming paradigms.
Python is widely used in web development and data science.
"""
analyze_text(sample)
