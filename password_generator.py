
import random
import string

print("===================================")
print("      SMART PASSWORD GENERATOR")
print("===================================")

# Get password length
length = int(input("Enter password length: "))

# Ask user for password requirements
uppercase = input("Include uppercase letters? (y/n): ").lower()
lowercase = input("Include lowercase letters? (y/n): ").lower()
numbers = input("Include numbers? (y/n): ").lower()
symbols = input("Include special symbols? (y/n): ").lower()

# Create character pool
characters = ""

if uppercase == "y":
    characters += string.ascii_uppercase

if lowercase == "y":
    characters += string.ascii_lowercase

if numbers == "y":
    characters += string.digits

if symbols == "y":
    characters += string.punctuation

# Generate password
if length <= 0:
    print("Password length must be greater than zero.")

elif not characters:
    print("Please select at least one character type.")

else:
    password = ''.join(
        random.choice(characters) for i in range(length)
    )

    print("\nYour Generated Password:", password)

    # Check password strength
    if length >= 12 and all([
        uppercase == "y",
        lowercase == "y",
        numbers == "y",
        symbols == "y"
    ]):
        print("Password Strength: Strong")
    elif length >= 8:
        print("Password Strength: Medium")
    else:
        print("Password Strength: Weak")
