# Kadane's Algorithm


def maxSubArray(nums):
    res = nums[0]
    t = 0

    for i in nums:
        if t < 0:
            t = 0
            
        t += i
        res = max(res, t)
        
    return res
    print(res)

    
    #if(n != 1):
    #    for i in range(n):
    #        for j in range(i,n):
    #            res = max(res, sum(nums[i:j+1]))
    #    return res
    #else:
    #    return nums[0]


    

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
