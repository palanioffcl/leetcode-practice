arr = [1,0,2,3,4]
pf = []
rsum = []
for j in arr:
    rsum.append(sum(arr[:j+1]))
print(rsum)
for i in arr:
    pf.append(i*(i+1)//2)
print(pf)
sarr = arr.sort()

sarr = sorted(arr)
spf = []

#print(sarr)

for j in sarr:
    spf.append(j*(j+1)//2)



#print(pf)
#print(spf)
res = 0
for k in range(len(arr)):
    if(pf[k] == spf[k]):
        res += 1

#print(res)
