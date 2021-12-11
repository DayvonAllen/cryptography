import string
from random import randint

ALPHABET = string.ascii_uppercase + " " + "," + "." + "'" + "1" + "2" + "3" + "4" + "5" + "6" + "7" + "8" + "9" + "0"


def encrypt(text, my_key):
    text = text.upper()
    cipher_text = ""

    for index, char in enumerate(text):
        key_index = my_key[index]
        char_index = ALPHABET.find(char)
        cipher_text += ALPHABET[(char_index + key_index) % len(ALPHABET)]

    return cipher_text


def decrypt(cipher_text, dec_key):
    plain = ""

    for index, char in enumerate(cipher_text):
        key_index = dec_key[index]
        char_index = ALPHABET.find(char)
        plain += ALPHABET[(char_index - key_index) % len(ALPHABET)]

    return plain


def random_sequence(text):
    random = []

    for _ in range(len(text)):
        random.append(randint(0, len(ALPHABET)))

    return random


message = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the " \
          "industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and " \
          "scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap " \
          "into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the " \
          "release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing " \
          "software like Aldus PageMaker including versions of Lorem Ipsum."

key = random_sequence(message)

encrypted_message = encrypt(message, key)

print(decrypt(encrypted_message, key))
