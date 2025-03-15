res = []
nums = [1,2,3,4]

for i in range(len(nums)):
    tmp = 1
    for j in range(len(nums)):
        if(i != j):
            tmp *= nums[j]
    print(tmp)
    res.append(tmp)

print(res)
