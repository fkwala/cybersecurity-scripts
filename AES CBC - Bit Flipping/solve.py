from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

key = b'\xfb\x38\xe0\xaf\xc8\x62\x8e\x9f\x59\x85\x30\x2a\xe7\x83\x29\xc7'
iv = b'\xd8\x9d\x1c\x9c\xd2\x24\x02\xf3\x70\x42\xd9\xdf\x03\xd3\x6e\x0c'
cipherText = b'\x80\x36\x0d\x31\x30\x67\x16\xdb\x29\x44\x15\xa1\xd1\x62\x9c\x7a\x89\xca\x30\xc0\x12\x2f\x7d\xed\x80\xcc\xbf\x35\x45\xbf\xc0\xb7'

cipher = AES.new(key, AES.MODE_CBC, iv)
paddedOriginalText = cipher.decrypt(cipherText)
originalTextBytes = unpad(paddedOriginalText, AES.block_size)
print(originalTextBytes) # feliciaSecurePwd

def xorBytes(s1, s2):
    return bytes(x ^ y for x, y in zip(s1, s2))

expectedText = "feliciaChangePwd"
expectedTextBytes = expectedText.encode()

xorDiff = xorBytes(originalTextBytes, expectedTextBytes)
modifiedIv = xorBytes(iv, xorDiff)

modifiedCipher = AES.new(key, AES.MODE_CBC, modifiedIv)
paddedModifiedText = modifiedCipher.decrypt(cipherText)

# Unpad the decrypted plaintext
modifiedText = unpad(paddedModifiedText, AES.block_size)
print(modifiedText) # feliciaChangePwd

def xorBytes(s1, s2):
    return bytes(x ^ y for x, y in zip(s1, s2))








