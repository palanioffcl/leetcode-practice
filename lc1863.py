nums = [5,1,6]
N = len(nums)




res = nums
res.append(nums[0]^nums[N-1])


for i in range(N):
    for j in range(i+1, N):
        print(nums[i:j])



        
for i in range(N):
    for j in range(i+1, N):
        tmp = 0
        for k in range(i,j+1):
            tmp ^= nums[k]
        print(tmp)
    res.append(tmp)

print(res)
