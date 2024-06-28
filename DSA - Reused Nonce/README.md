# Digital Signature Algorithm (DSA) - Reused Nonce K

### Problem Statement

Attempt to generate a valid signature for a fake message, in order to impersonate the original sender.

### Attack Description

The main vulnerability is the reuse of the nonce **_k_**, which can expose **_k_** through some calculation, and ultimately expose the private key **_x_**. Once **_x_** is exposed, the attacker can impersonate the original sender to send any message.

### Solution Description

Since s = (k ^ −1) \* (m + xr) mod q and we have 2 **_s_** values that used the same **_k_**, we can make an equation for **_s1 - s2_** and rearrange the resulting equation:

k = (m1 - m2) \* pow(s1 - s2, -1, q) mod q

We can insert this value of **_k_** into this equation to find **_x_**:

x = (sk - m) \* (r ^ -1) mod q

After finding **_x_**, we can use the same public key **_y_** to generate new valid signatures, \***_fakeR_** and **_fakeS_** in this case, to impersonate the original sender.
