import random
def generate_password(length):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    return ''.join(random.choice(chars) for _ in range(length))

length = int(input("Enter password length (minimum 5): "))
if length < 5:
    print("Password must be at least 5 characters long.")
else:
    password = generate_password(length)
    print("Generated password:", password)