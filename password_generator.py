import random
import string

def generate_password():
    print("Welcome to the Password Generator!")

    try:
        length = int(input("Enter desired password length (minimum 4): "))
        if length < 4:
            print("Password must be at least 4 characters long.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    # Ask what to include
    include_letters = input("Include letters? (y/n): ").lower() == 'y'
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    if not (include_letters or include_digits or include_symbols):
        print("You must select at least one character type.")
        return

    characters = ""
    if include_letters:
        characters += string.ascii_letters  # a-z + A-Z
    if include_digits:
        characters += string.digits         # 0-9
    if include_symbols:
        characters += string.punctuation    # Special characters

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"\n✅ Generated Password: {password}")

# Run the function
generate_password()
