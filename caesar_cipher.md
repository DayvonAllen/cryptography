## Caesar-Cipher
- It is a private key encryption(symmetric encryption) method
- It was first used by Julius Caesar over 2000 years ago
- It is a type of substitution cipher: we shift every single letter in the plaintext with a fixed number of letters.
- The key itself is the number of letters we use for shifting
- First we assign numerical values to every letter in the alphabet to be able to use mathematical operations during encryption/decryption
- Encryption algorithm:
  - `E(x) = (x + n) % 26`
  - We have to consider all the characters in the plaintext
  - `E(x)` is the encrypted letter of the original `x` letter.
  - We have to shift the given letter with `n`(where `n` is the key)
  - Why use `% 26`? The size of the english alphabet is 26 which means there are 26 letters in the english alphabet.
  - We want to make sure the encrypted letter is within the range of `[0, Size Of the Alphabet]`, so the is why we use `% 26`
- Decryption algorithm:
  - `D(x) = (x - n) % 26`
  - We have to consider all the characters in the plaintext
  - `D(x)` is the decrypted letter(x is the letter in the ciphertext).
  - We have to shift the given letter with `-n`(where n is the key)
  - Why use `% 26`? The size of the english alphabet is 26 which means there are 26 letters in the english alphabet.
  - We want to make sure the encrypted letter is within the range of `[0, Size Of the Alphabet]`, so the is why we use `% 26`
- Can use bruteforce against this not a good encryption technique.
- Can also use `frequency-analysis`(we can analyze the frequency distribution of the letters)
  - For example in english text some letters are more frequent than others(E, A, O, I and T)
    - We can analyze the ciphertext and based on the most frequent letter in the ciphertext we can predict the key(so the number of shifts)
---
    
## Frequency Analysis Cracking
1. Calculate the relative frequency distribution of the ciphertext's letter
2. Get the most frequent letter in the ciphertext(or the second because the most frequent one may be white-spaces)
3. We can get the key based on a simple formula
   1. Key = value of ciphertext's most frequent letter - value of E
- We are able to crack `Caesar-cipher` because some information is revealed about the crypto-system
  - This is called "information leak"
  - Because of the leaking information we can analyze ciphertexts and crack the given cipher
  - Information leaks can be avoided by using random numbers
    - this is why one-time-pad(OTP) came to be.
    - OTP prevents information leaks and we are not able to crack it using frequency analysis.
---