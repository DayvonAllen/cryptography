## Types Of Encryption
- Knowledge of discrete mathematics and prime numbers helps you understand encryption.
- Symmetric Encryption(Private Key Cryptography):
  - This type of cryptography uses a single key, the same key is used for both encryption and decryption.
  - Mathematical function + the private key is used to generate the ciphertext.
  - Ex. AES, DES, Caesar-cipher
  - Main problem is that the key must be exchanged.
- Asymmetric Encryption(Public Key Cryptography):
  - This type of cryptography uses a public key and private key.
  - We have to keep the private key secret but the public key should be known.
  - Messages encrypted with a public key can only be decrypted by the private key generated with that public key.
  - Mathematical function + the public key is used to generate the ciphertext.
  - How it works(Example):
    1. If Alice wants to send a message to Bob then Alice will encrypt it with Bob's public key
    2. Bob can decrypt the message with his private key.
  - Ex. RSA, Elliptic Curve Cryptography
---