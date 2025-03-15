#nums = [4,4,4,4]
#nums = [1,2,2,3,3,4]
#nums = [7,9,7,7,7,5]
#nums = [8,8,10,9,9]
nums = [10,8,8,7,7]
k = 1

nums.sort()
res = 0
prev = nums[0]-k

for i in nums:
    lb = i-k
    ub = i+k

    if(prev < lb):
        prev = lb
        res += 1
    elif prev < ub:
        prev += 1
        res  += 1
        
print(res)
