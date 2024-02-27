def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_index = {char: index for index, char in enumerate(alphabet)}
    final_message = []

    for char in message.lower():
        if not char.isalpha():
            final_message.append(char)
        else:
            key_char = key[key_index % len(key)]
            key_index += 1

            offset = alphabet_index[key_char]
            index = alphabet_index[char]
            new_index = (index + offset * direction) % len(alphabet)
            final_message.append(alphabet[new_index])

    return ''.join(final_message)


def encrypt(message, key):
    return vigenere(message, key)


def decrypt(message, key):
    return vigenere(message, key, -1)


message = input("Enter your message: ")
key = input("Enter your key: ")
choice = input("Do you want to encrypt or decrypt the message? Enter 'e' for encrypt and 'd' for decrypt: ")

if choice.lower() == 'e':
    result = encrypt(message, key)
    print(f'\nEncrypted text: {result}\n')
elif choice.lower() == 'd':
    result = decrypt(message, key)
    print(f'\nDecrypted text: {result}\n')
else:
    print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")
