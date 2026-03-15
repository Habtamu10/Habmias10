# Palindrome Check
def is_palindrome(s):
    s = "".join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

def is_palindrome_number(x):
    if x < 0:
        return False
    return str(x) == str(x)[::-1]

print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("race a car"))                       # False
print(is_palindrome_number(121))                         # True
print(is_palindrome_number(-121))                        # False
