import re
import secrets
import string


def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)

        constraints = [
            (nums, r'\d'),
            (special_chars, fr'[{symbols}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]

        # Check constraints
        if all(
                constraint <= len(re.findall(pattern, password))
                for constraint, pattern in constraints
        ):
            break

    return password


def main():
    customize = input("Would you like to customize the requirements of the password? (y/n): ")
    if customize == "yes".lower() or customize == "y".lower():
        length_ = int(input("Please enter the length of the password: "))
        numbers = int(input("Please enter how many numbers should the password contain: "))
        special = int(input("Please enter the number of special characters: "))
        upper_ = int(input("Please enter the number of uppercase letters: "))
        lower_ = int(input("Please enter the number of lowercase letters: "))
        new_password = generate_password(length=length_,
                                         nums=numbers,
                                         special_chars=special,
                                         uppercase=upper_,
                                         lowercase=lower_)
    else:
        new_password = generate_password()
    print('Generated password:', new_password)


if __name__ == '__main__':
    main()
