# Digital Signature Algorithm (DSA) - Leaked Nonce K

### Problem Statement

Attempt to generate a valid signature for a fake message, in order to impersonate the original sender.

### Attack Description

The main vulnerability is the exposure of the nonce **_k_**, which can ultimately expose the private key **_x_**. Once **_x_** is exposed, the attacker can impersonate the original sender to send any message.

### Solution Description

The signature **_(r,s)_** and message (hashed version can be calculated) are public. Since **_k_** is given, we can manipulate this equation:

s = (k ^ −1) \* (m + xr) mod q

By rearranging the equation, we get:

x = (sk - m) \* (r ^ -1) mod q

After finding **_x_**, we can use the same public key **_y_** to generate new valid signatures, \***_fakeR_** and **_fakeS_** in this case, to impersonate the original sender.
