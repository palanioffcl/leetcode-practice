nums = [963,-626,963]

N = len(nums)
for i in range(N):
    for j in range(N):
        totSum = sum(nums[i:j])
        if(totSum in nums and abs(j-i) == N-2):
            nums.remove(totSum)
            del nums[i:j]
print(nums[0])
