import string

ALPHABET = string.ascii_uppercase + " " + "," + "?" + "'"


def vigenere_encrypt(plain_text, key):
    plain_text = plain_text.upper()
    key = key.upper()

    cipher_text = ""
    key_index = 0

    for character in plain_text:
        index = (ALPHABET.find(character) + ALPHABET.find(key[key_index])) % len(ALPHABET)

        cipher_text = cipher_text + ALPHABET[index]

        if key_index == len(key) - 1:
            key_index = 0
        else:
            key_index = key_index + 1
    return cipher_text


def vigenere_decrypt(cipher_text, key):
    cipher_text = cipher_text.upper()
    key = key.upper()

    plain_text = ""
    key_index = 0

    for character in cipher_text:
        index = (ALPHABET.find(character) - ALPHABET.find(key[key_index])) % len(ALPHABET)

        plain_text = plain_text + ALPHABET[index]

        if key_index == len(key) - 1:
            key_index = 0
        else:
            key_index = key_index + 1
    return plain_text


print(vigenere_encrypt("this is just an example", "secret"))
print(vigenere_decrypt("HLKFA,GALHWIOEPNIMSQR?I", "secret"))
