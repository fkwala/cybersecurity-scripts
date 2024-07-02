# Compilation of Cybersecurity Learnings

All problems/attacks are categorized into their own folders. Each folder contains the solve.py script and the README.md file which containts the vulnerability and script walkthrough.

### Other Executed Attacks

#### AES CBC - Padding Oracle Attack

The padding oracle attack is possible due to 2 vulnerabilities:

1. AES CBC encryption being solely based on XOR functions between its blocks
2. The usual padding method is predictable: calculate how many bytes to add and add that many copies of ASCII byte to the end (e.g. b'\x03\x03\x03')

The main objective is to figure out the entire plaintext without needing to decrypt the ciphertext. This attack is possible if the attacker is given a server that accepts ciphertext inputs and outputs whether the result is valid or not.

Let C(i) be the current ciphertext block, P(i) be the current plaintext block, C(i-1) be the previous ciphertext block,

1. Use a for loop to generate all 256 numbers of C(i-1) with modified last byte (e.g. \x00,\x01...\xff)
2. Input all 256 numbers into the system. This allows the modified C(i-1) to XOR with the decrypted C(i)
3. Find the C(i-1) value that produces an incorrect value (not correct / padding error). We know that the last P(i) byte is \x01
4. Repeat Steps 1 to 3 until the first byte of C(i-1).
5. At this point, the modified C(i-1) should produce P(i) = b'\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10'
6. Due to the self-inversibility of XOR functions, decrypted C(i) = b'\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10' ^ modified C(i-1)
7. P(i) = decrypted C(i) from Step 6 ^ original C(i-1)
8. Repeat Steps 1 to 7 for the remaining blocks, where the previous ciphertext block for C(i) is the IV
