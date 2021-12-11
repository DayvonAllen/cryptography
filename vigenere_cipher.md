## Vigenere Cipher
- It is very similar to the Caesar crypto-system, but we use several keys instead of just a single key.
- `Vigenere crypto-system` is a method of encrypting alphabetic text by using a series of interwoven caesar ciphers based on the letters of a keyword.
- It is a form of poly alphabetic substitution method
- very easy to understand and to implement
- It was constructed in the 16th century, and it was thought to be unbreakable.
- It tries to fix the problem with caesar cipher(there are so few possible keys for the english language, 26)
- Vigenere cipher uses a given word as the private key
  - Ex. key = `Secret`(the letters in the key have to be converted into integers first)
- The numerical representations of the letters in the key define how many characters to shift the actual letter in the plaintext.
- Instead of using a single value as the key(like caesar cipher), we have as many values as the number of letters in the private key.
- Size of the keyspace = 26^<size of the key>
  - Ex. key = `Secret`, keyspace = 26^6(because "secret", is 6 letters)
- Encryption:
  - `E<sub i>(x<sub i>) = (x<sub i> + K<sub i>) % 26`
  - We have to use the same formula as caesar cipher
  - `x<sub i>` is the actual letter in the plaintext
  - `E<sub i>(x<sub i>)` is the encrypted letter in the ciphertext
  - In Vigenere cipher we have to use the `i-th` letter of the ket for encrypting the `i-th` letter
- Decryption:
  - `D<sub i>(x<sub i>) = (x<sub i> - K<sub i>) % 26`
  - We have to use the same formula as caesar cipher
  - `x<sub i>` is the actual letter in the plaintext
  - `D<sub i>(x<sub i>)` is the decrypted letter in the ciphertext
  - In Vigenere cipher we have to use the `i-th` letter of the ket for encrypting the `i-th` letter
``` 
  private key equals "secret"
  
  Plain Text = This is just an example
  
  add the index of the secret letter to the current letter and shift like we are doing the caesar cipher
  
  Secr et Secr et secrets
  this is just an example
  (37 % 26)(11)(10)(35 % 26) = this(new index after adding "secr" to each char)
``` 
- We can crack this cryptographic method using dictionary attacks(brute force, not a good way) and Kasiski-algorithm(a smart approach to cracking vigenere cipher)
---

## Kasiski Algorithm
- It was constructed by Friedrich Kasiski in 1863
- If we know the size of the key then we can use frequency analysis in order to decrypt a given ciphertext(we will take advantage of information leaks)
- Algorithm:
  - We have to find the size of the key: we can analyze repeated substrings and their factors to get a good guess
  - We can construct substrings from the ciphertext that are encrypted by the same letters
  - We can use frequency analysis to find the letters of the keys.
---