def searchRange(nums, target):
    res = []
    if(len(nums) == 1 and target in nums):
        return [0,0]
    else:
        for i in range(len(nums)-1):
            if(nums[i] != nums[i+1] and nums[i+1] == target):
                res.append(i+1)
            elif(nums[i] != nums[i+1] and nums[i] == target):
                res.append(i)
        if(len(res) == 0):
            return [-1,-1]
        else:
            return res

print(searchRange([1],1))
