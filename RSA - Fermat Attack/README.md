# RSA Encryption - Fermat Attack

### Problem Statement

Attempt the Fermat Attack to retrieve the decrypted flag given n, e, and the encrypted flag.

### Attack Description

The security of RSA is based on the hardness of factoring out the primes **_p_** and **_q_** from **_n_**. However, if **_p_** and **_q_** are close to each other, the difference is small enough such that the attacker can use the Fermat's Factorization Method to derive **_p_** and **_q_** from **_n_**.

### Solution Description

Fermat's Factorization Method:
Let p = a+b and q = a-b,
n = (a + b)(a - b) = a^2 - b^2

Since the difference is small, we can assume that **_a_** is close to the square root of **_n_**. Rearranging the factorization formula, b = sqrt(a^2 - n). Hence, by increasing **_a_** and checking if **_a^2 - n_** is a perfect square, we can find both **_a_** and **_b_**. Consequently, we can calculate **_p_** and **_q_** and solve for **_d_** to decrypt the encrypted flag.
The decodedString should be "feliciaSampleFlag".
