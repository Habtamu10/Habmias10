# Password Generator
import random
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_special=True):
    chars = string.ascii_lowercase
    if use_upper:   chars += string.ascii_uppercase
    if use_digits:  chars += string.digits
    if use_special: chars += "!@#$%^&*"

    password = [random.choice(string.ascii_lowercase)]
    if use_upper:   password.append(random.choice(string.ascii_uppercase))
    if use_digits:  password.append(random.choice(string.digits))
    if use_special: password.append(random.choice("!@#$%^&*"))

    while len(password) < length:
        password.append(random.choice(chars))

    random.shuffle(password)
    return "".join(password)

for i in range(5):
    print(f"Password {i+1}: {generate_password(16)}")
