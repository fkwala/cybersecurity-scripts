# DJB2 Hash Function - Preimage Attack

### Problem Statement

Attempt the Preimage Attack on a DJB2 hash ending with 0xaee878a9.

DJB2 Hash Function:
def hash_djb2(s):
h = 5381
for x in s.encode():
h = ((h \* 33) + x) & 0xFFFFFFFF
return h

### Attack Description

As the DJB2 Algorithm solely consists of multiplication and addition operations, it is easy to reverse to find the preimage.

### Solution Description

Working backwards on the DJB2 algorithm, the correct preimage is found for the corresponding hash if we can reverse the hash to 5381.

In order to reverse "h = ((h \* 33) + x) & 0xFFFFFFFF":

1. Calculate y = hash % 33
2. Find a character (ASCII 33 to 122) such that y = x % 33
3. We find y == hash % 33 == x % 33. In the original equation "(h _ 33) + x", since h _ 33 % 33 == 0, the remainder of hash % 33 will reduce to x % 33.

By repeating this reversal through recursion, we can find multiple correct preimages and its hash.

Note: I narrowed the range in the for loop to 1610 - 1620 as only this range produces corresponding preimages.
