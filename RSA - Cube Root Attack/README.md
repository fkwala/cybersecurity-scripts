# RSA Encryption - Cube Root Attack

### Problem Statement

Attempt the cube root attack to retrieve the decrypted flag given n, e, and the encrypted flag.

### Attack Description

When the exponent **_e_** is small, the message may be easily deducible without needing the private key **_d_**.
Rearranging the equation **_encrypted flag = (message ^ e) % n_**, we get **\_encrypted flag + kn = message ^ e** for some unknown variable **_n_**. Since the exponent **_e_** is small, the value of k is small and easily brute-forceable.

### Solution Description

Working backwards, we need to find the valid **_k_** such that we can take the root of **_encrypted flag + kn_** by **_e_** perfectly (no remainders). At the same time, as we take the result of root of **_encrypted flag + kn_** by **_e_**, the result is the decrypted message.
The decodedString should be "feliciaSampleFlag".
