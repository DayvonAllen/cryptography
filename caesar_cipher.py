import string

# All alphabets in uppercase
ALPHABET = string.ascii_uppercase + " " + "," + "?" + "'"
KEY = 23


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


message = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the " \
             "industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and " \
             "scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap " \
             "into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the " \
             "release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing " \
             "software like Aldus PageMaker including versions of Lorem Ipsum."

encrypted_message = caesar_encrypt(message)
print(encrypted_message)
# print(caesar_decrypt(encrypted_message))
