import string
import random

def generater_password(name, digit):
    name = name
    characters = string.ascii_letters + string.digits + "!@#$%^&*()_+[]{}|;:,.<>?"
    return name[:3] + ''.join(random.choice(characters) for i in range(digit))

name = input("Enter your name: ")
user_input = int(input("Enter the length of the password: "))

if user_input < 8:
    print("Password length should be at least 8 characters.")
else:
    result = generater_password( name,user_input)
    print("Generated password:", result)


