# RSA Encryption - Known Partial Prime Number

### Problem Statement

Attempt to retrieve the decrypted flag given n, e, part of p, q, and the encrypted flag.

### Attack Description

The security of RSA is based on the hardness of factoring out the primes **_p_** and **_q_** from **_n_**. With **_q_** and part of **_p_** known, as well as **_n_** and **_e_** being the public key, this makes the private key **_d_** vulnerable to being revealed. By extension, this makes it easy to decode the given flag.

### Solution Description

The main objective is to find the private key **_d_** to decrypt the flag. Since **_n_** = **_p_**\***_q_**, the last 3 nibbles of **_p_** can be derived.
Using a for loop to go through all possible values for the last 3 nibbles of **_p_**, we can find the actual **_p_** if it fulfills:

1. **_p_** is a prime number
2. **_n_** is perfectly divisible by **_p_**

Once **_p_** is found, the private key **_d_** can be calculated with **_d = pow(e, -1, phi of n)_**.The flag can then be decoded using the private key **_d_**. The decodedString should be "feliciaSampleFlag".
