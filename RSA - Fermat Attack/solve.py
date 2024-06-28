from Crypto.Util import number
import gmpy2

e = 65537
n = 0xcdab185e41cc40659b00179c24564aed4fcf55b9504e9a32629a3efa17aa1cfc10d23a05a792e45cccd002e0d19dfa57b7c382b40eb13fb5ac0ef72b400a22231757085c59151957939a9c65784f85b41e11856568b5525af127ce03c3f710123e6c288fb3e74bcf0dfeb565a0d9ad3ff7dd44c28cb0daca27e2a2b32a8fcbadf29b5048378c839b581f59a4c7887eef523d54081b46ae4f30651009353ef5446e44fa63c2d856c7f0490222a256998e33f842b85a3c3323c62c175d921ffa4f62e3bf556bcea6e185f2ec2519373a3114cc7b25c7cb49a25cf71d4c14c7733697bfb21a4aa30c00b90148adee635a57fa5d6322b8090218c0085f2014bbb397
flag = 0x6183f9abb313b98c4c9f48fc8f49c41b2bb6fdf0c0d965ec9213b455c7eaa0a91f174cbe294df51a49e33598a0b894628f6f4d6404871d5218c3d9ead5b0492aedbf0c1207d5dc4eb4ded2b6169491e7ba16827bbbbb3782ed6b10ecd163b9641dfceceb0f28109591c0c1454796e3be7cc49818c924d4aaf5bf2a00fd4c053347e88a10ce6cae8fff76d536a714cb56e3cc93b43fa87dca64e1f5a9427b2ed3ec001fc4f61e220255cd7911f929d0b8d837ebdbc09da6586ba741d30ac3e343776511722332f5ab1199121ae13bb928d16458ba3c8ff9dd055394c96e690815a06f8becd4e4d5ab7c8c79c37c40452c5e55f6bb2e82a9256c588fd306e1928e

a = int(gmpy2.isqrt(n)) 
b_squared = a ** 2 - n 

while not gmpy2.is_square(b_squared):
    a += 1 
    b_squared = a ** 2 - n 
    
b = int(gmpy2.isqrt(b_squared))
p = a - b 
q = a + b 

phiN = (p-1)*(q-1)
d = number.inverse(e, phiN)
decryptedFlag = pow(flag, d, n)
byteString = decryptedFlag.to_bytes(decryptedFlag.bit_length(), 'big')
decodedString = byteString.decode('utf-8')
print(decodedString)


