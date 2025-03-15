from math import *

gifts = [56,41,27,71,62,57,67,34,8,71,2,12,52,1,64,43,32,42,9,25,73,29,31]
k = 52

for i in range(k):
    print(gifts)
    currMax = max(gifts)
    for i in range(len(gifts)):
        if gifts[i] == currMax:
            gifts[i] = int(sqrt(currMax))
            break
print(sum(gifts))
