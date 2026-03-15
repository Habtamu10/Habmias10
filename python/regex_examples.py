# Python Regular Expressions
import re

text = "Contact us at support@example.com or info@company.org"

emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
print("Emails:", emails)

phones = ["0911234567", "011-123-4567", "invalid", "+251911234567"]
pattern = r"^(\+251|0)9\d{8}$"
for phone in phones:
    valid = bool(re.match(pattern, phone.replace("-", "").replace(" ", "")))
    print(f"  {phone}: {'valid' if valid else 'invalid'}")

cleaned = re.sub(r"\s+", " ", "Hello   World  from   Python")
print("Cleaned:", cleaned)
