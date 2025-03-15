def maxSubarraySum(nums, k):
    N = len(nums)
    maxSum = -100000
    if(len(nums) == 1):
        return nums[0]
    else:
        for i in range(N):
            for j in range(N):
                curr = sum(nums[i:j+1])
                if(len(nums[i:j+1]) % k == 0 and maxSum  < curr):
                    maxSum = curr

        if(maxSum == 0):
            return -1
        else:
            return maxSum


print(maxSubarraySum([-1,-2, -3, -4, -5], 4))
