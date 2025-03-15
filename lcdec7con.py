nums = [5,2,5,4,5]
k = 2

for i in nums:
    if(i < k):
        print(-1)

print("hii") 
res = 0
print(set(nums))


while(len(set(nums)) != 1):
    nums.sort()
    preMax = list(set(nums))[-2]            
    for j in range(len(nums)):
        if nums[j] > preMax:
            nums[j] = preMax
    res += 1
print(res)
