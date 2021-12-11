import string

ALPHABET = string.ascii_uppercase + " " + "," + "?" + "'"

potential_answer = {}


def crack_caesar(cipher_text):
    plain_text = ""

    cipher_text = cipher_text.upper()

    for KEY in range(len(ALPHABET)):
        print(KEY)
        for c in cipher_text:
            index = ALPHABET.find(c)
            index = (index - KEY) % len(ALPHABET)
            plain_text = plain_text + ALPHABET[index]
        potential_answer[KEY] = plain_text
        plain_text = ""

    return plain_text


crack_caesar("A,RTMA,K,UTAHPWLTBMT'HBG'V")

print(potential_answer)
