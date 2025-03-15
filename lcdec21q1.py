nums = [1,2,1,4,1]
res = 0

N = len(nums)

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1, N):
            if(nums[i] + nums[k] == nums[j]/2) and len(nums[i:k+1]) == 3:
                print(nums[i:k+1])
                res += 1

print(res)
