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
- `One time pad's keyspace = 26^<size of the plaintext>`
---
     
## Pseudo-Random Number Algorithms
- Computers are inherently deterministic, so it is impossible to define algorithms to generate true random numbers.
- But we can generate pseudo-random numbers with these algorithms:
  - `Middle-Square Method`
    - Invented by John von Neumann in 1949
    - Input is the seed, the seed should be different(like unix time)
    - Algorithm:
      - Multiply the seed by itself
      - get the middle of the result
      - the result is the seed in the next iteration
    - The randomness of the sequence depends on the randomness of the seed exclusively. 
  - `Mersenne Twister`
  - `Linear Congruential Generators`
    - `X<n + 1> = (a X<n> + c) % m`
    - as usual, we have to define a seed which is thee `x<0>`
    - The values of the parameters `a`, `c` and `m` determine the period
---