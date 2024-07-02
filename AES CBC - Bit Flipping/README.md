# AES CBC Encryption - Bit Flipping Attack

### Problem Statement

Attempt the Bit Flipping Attack to change the plaintext given the ciphertext, key, and IV. This attack could happen in a login verification system where an attacker cannot modify the original plaintext but can produce a decrypted output that is the same as the plaintext.

### Attack Description

The vulnerability of AES CBC is due to it solely based on XOR functions. In the decryption process, the plaintext block i is formed by XORing ciphertext block i-1 and decrypted ciphertext block i. Hence, since the attacker is given the Ciphertext (or IV if we want to manipulate plaintext block 1), the attacker can manipulate ciphertext block i-1 to manipulate the next plaintext block.

### Solution Description

The objective is to flip the bits of the original plaintext from "feliciaSecurePwd" to "feliciaChangePwd".

Let P(i) be the plaintext block we want to modify, P'(i) be the modified plaintext block, C(i) be the corresponding ciphertext block, and C(i-1) be the ciphertext of the previous block.

Since XOR is self-inversible, I got the XOR Difference (xorDiff) between P(i) and P'(i). Since the change is in P(1), C(0) is the IV. Hence I XORed xorDiff with IV to produce IV'. Lastly, I decrypted the ciphertext with the modified IV, to get the modified plaintext "feliciaChangePwd".
