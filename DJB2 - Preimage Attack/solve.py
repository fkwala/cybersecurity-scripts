def reverse(hash, result):
    if hash == 5381:
        print(result)
        return
    elif hash > 5381:
        y = hash % 33
        for x in range(33, 123):
            if x % 33 == y:
                result = chr(x) + result
                reverse((hash - x) / 33, result)
                result = result[1:]

for i in range(1610,1620):  
    hash = "0x" + format(i, 'x') + "aee878a9"
    print(hash)
    reverse(int(hash, 16), "")