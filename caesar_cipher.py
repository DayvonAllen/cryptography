import string

# All alphabets in uppercase
ALPHABET = string.ascii_uppercase
KEY = 3


def caesar_encrypt(plain_text):
    cipher_text = ""

    plain_text = plain_text.upper()
    #  consider all letters
    for c in plain_text:
        # find the numerical representation (index) associated with that character in the alphabet
        index = ALPHABET.find(c)
        # E(x) = (x + n) % 26 encryption formula
        index = (index + KEY) % len(ALPHABET)
        cipher_text = cipher_text + ALPHABET[index]

    return cipher_text


def caesar_decrypt(cipher_text):
    plain_text = ""

    cipher_text = cipher_text.upper()
    #  consider all letters
    for c in cipher_text:
        # find the numerical representation (index) associated with that character in the alphabet
        index = ALPHABET.find(c)
        # E(x) = (x - n) % 26 decryption formula
        index = (index - KEY) % len(ALPHABET)
        plain_text = plain_text + ALPHABET[index]

    return plain_text


print(caesar_encrypt("Hello"))
print(caesar_decrypt("KHOOR"))
