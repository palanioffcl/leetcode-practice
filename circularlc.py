x = [5,7,1,4]
k = 3

res = []

for i in range(len(x)):
    kdigitsum = 0
    for j in range(i,k-1):
        kdigitsum += x[i+j%len(x)]
    res.append(kdigitsum)


print(res)
