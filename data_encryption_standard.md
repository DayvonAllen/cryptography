## Data Encryption Standard(DES)
- DES is a symmetric-key algorithm
- It was constructed in the early 1970s at IBM(designed mostly by Horst Feistel)
- It is a block cipher: the plaintext is processed to the ciphertext in a number of blocks
- Hybrid of substitution cipher and permutation cipher
  - We are not able to use frequency analysis to crack `DES`
- DES has a so-called `Feistel-Structure`
  1. We have to split the plaintext(convert to binary first) into 64 bit long blocks
     1. These blocks are the input for the 16 rounds
  2. There are `rounds`(iteration) during the encryption/decryption
     1. For DES there are 16 rounds(substitutions, XOR operations etc.)
        1. The input for every iteration is a 64 bit block.
  3. Every round needs different keys(these are called sub-keys)
     1. These keys are generated from the original 64 bits private key
  4. It's main advantage is that encryption and decryption operations are very similar(requiring only the reversal of the key schedule)
     1. `Block Size`: 64 bits
     2. `Key Size`: 64 bits(56 relevant bits are used in the algorithm)
     3. `Number of Rounds`: 16
     4. `Number of Subkeys`: 16(every subkey is 48 bits long)
     5. `Ciphertext Size`: 64 bits
- `Circular Shift`(Bitwise rotation) - is an operator that shifts all the bits we want to shift `01001000`(first digit is the most significant digit and the last is the least significant digit) to the left then the result will be `10010000`
  - In `DES` we sometimes shift by 1, and sometimes we shift by 2.
---
     
## How DES works
1. First we convert the plaintext into binary
2. Split the binary representation of the plaintext into 64 bit long blocks(64 bits of binary)
3. Those blocks will be the input to the DES algorithm.
4. We are going to use the 64 bits private key and the block to generate the ciphertext.
5. We use the Initial Permutation(IP) that's going to change the location of the bits in the 64 bits block
   1. We shuffle the order of the bits in the block
6. We have to generate the 16 sub-keys
   1. Steps to generate a sub-key:
      1. We have to apply the `Permuted Choice 1(PC-1)` To shuffle the order of bits and omit 8 bits(output contains 56 bits) in the 64 bits private key
      2. Then we apply `left circular shift`(shift all the bits to the left) operation in order to get the sub-key for the first round(56 bits)
      3. We then use `Permuted Choice 2(PC-2)` to convert the sub-key to 48 bits
7. The output of the first round will be the input to the second round etc.
8. We apply the above for 16 rounds
9. After the last round we have to use `32 bit swap`(left half<32 bits> and right half<32 bits> are swapped)
10. We have to use `Inverse Permutation`(IP^-1) to get the ciphertext.
---