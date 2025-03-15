nums = [1,2,3,4]
print(nums,"NUMS")
res = []

maxnum = max(nums)
print(maxnum, "MAX")

for i in nums:
    res.append(i*2)

print(res, "RES")

for i in res:
    if(maxnum >= i):
        for k in nums:
            if(k == maxnum):
                print(k)
    else:
        print(-1)
