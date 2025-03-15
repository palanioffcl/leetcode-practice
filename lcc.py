def areAllBitsSet(n):
    if set(n) == {'1'}:
        return True
    else:
        return False


n = 1000
if areAllBitsSet(bin(n)[2:]):
    print(n)
else:
    for i in range(n+1,10000):
        if areAllBitsSet(bin(i)[2:]):
            print(i)
            break

