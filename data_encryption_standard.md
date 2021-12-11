## Data Encryption Standard(DES)
- DES is a symmetric-key algorithm
- it was constructed in the early 1970s at IBM(designed mostly by Horst Feistel)
- it is a block cipher: the plaintext is processed to the ciphertext in a number of blocks
- hybrid of substitution cipher and permutation cipher
  - we are not able to use frequency analysis to crack `DES`
- DES has a so-called `Feistel-Structure`
  1. We have to split the plaintext(convert to binary first) into 64 bit long blocks
     1. these blocks are the input for the 16 rounds
  2. There are `rounds`(iteration) during the encryption/decryption
     1. for DES there are 16 rounds(substitutions, XOR operations etc.)
        1. the input for every iteration is a 64 bit block.
  3. Every round needs different keys(these are called sub-keys)
     1. These keys are generated from the original 64 bits private key
  4. It's main advantage is that encryption and decryption operations are very similar(requiring only the reversal of the key schedule)
     1. `Block Size`: 64 bits
     2. `Key Size`: 64 bits(56 relevant bits are used in the algorithm)
     3. `Number of Rounds`: 16
     4. `Number of Subkeys`: 16(every subkey is 48 bits long)
     5. `Ciphertext Size`: 64 bits
---