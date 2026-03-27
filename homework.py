import random
import string

def generate_password(length=12):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits)
    ]

    all_chars = lower + upper + digits
    password += random.choices(all_chars, k=length - 3)
    
    random.shuffle(password)
    
    return ''.join(password)

print("Generated Password:", generate_password(12))