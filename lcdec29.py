#nums = [1,2,3,4,3,6,1]
nums = [3,4,3,4,3,4,3,4]

res = 0
n = len(nums)


nums.sort()

for p in range(n):
    for q in range(p+1, n):
        l = q+1
        r = n-1
        while l<q:
            if(nums[p] * nums[l] == nums[q] * nums[r]):
                res += 1
            elif(nums[p] * nums[l] < nums[q] * nums[r]):
                l += 1
            elif(nums[p] * nums[l] == nums[q] * nums[r]):
                r -= 1

#for p in range(n):
#    for q in range(p+1,n):
#        for r in range(q+1,n):
#            for s in range(r+1,n):
#                if((nums[p] * nums[r]) == (nums[q] * nums[s]) and q-p > 1 and r-q > 1 and s-r > 1):
#                    res += 1

print(res)
