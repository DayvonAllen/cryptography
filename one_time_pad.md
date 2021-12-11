## One Time Pad(OTP)
- It was constructed by Frank Miller in 1882
- It uses totally random numbers to shift the letters in the plaintext
  - the key must have the same size as the plaintext
  - the key must contain random numbers
  - we can eliminate information leaks with random numbers
- Algorithm:
  1. generate a truly random sequence(as many random numbers as the letters in the plaintext)
     1. Do not reuse the same numbers over and over again
     2. the private key is used one time as well(it is not reused for other messages)
  2. Shift the letters in the plaintext with the random numbers in the same manner as in the vigenere cipher or caesar cipher
     1. There will be no information leak is you use this approach because every letter in the ciphertext is equally likely.
     2. Kasiski Method does not work against this.
---