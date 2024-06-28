import gmpy2

e = 3
n = 0xe46c9591f030307d1b63c73e3cf6a3c632b73607e357d0219734f2c3baf1ccf67b2633a7b74b5395326c1768b34262c0c3039b349625b639d352cf0fbdc488fd5724d9baf0af76ab8ae47daebcc1f41afef9d97c69d2ae7483fa3c0fa8378d65f3ef672ef576ccd233b5da8086ed382fa95936ae12ad0f2e9df6c9a81b
flag = 0x6183f9abb313b98c4c9f48fc8f49c41b2bb6fdf0c0d965ec9213b455c7eaa0a91f174cbe294df51a49e33598a0b894628f6f4d6404871d5218c3d9ead5b0492aedbf0c1207d5dc4eb4ded2b6169491e7ba16827bbbbb3782ed6b10ecd163b9641dfceceb0f28109591c0c1454796e3be7cc49818c924d4aaf5bf2a00fd4c053347e88a10ce6cae8fff76d536a714cb56e3cc93b43fa87dca64e1f5a9427b2ed3ec001fc4f61e220255cd7911f929d0b8d837ebdbc09da6586ba741d30ac3e343776511722332f5ab1199121ae13bb928d16458ba3c8ff9dd055394c96e690815a06f8becd4e4d5ab7c8c79c37c40452c5e55f6bb2e82a9256c588fd306e1928e

for k in range(20):
    newFlag = flag + k*n
    res, rem = gmpy2.iroot_rem(newFlag, e)
    if rem == 0:
        decryptedFlag = int(res)
        byteString = decryptedFlag.to_bytes(decryptedFlag.bit_length(), 'big')
        decodedString = byteString.decode('utf-8')
        print(decodedString)