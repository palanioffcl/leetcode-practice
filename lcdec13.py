nums = [2,1,3,4,5,2]

# nums = [0,0,0,4,5,2]

score = 0


while set(nums) != {0}:
    minNum = min(nums)
    print(minNum, "minNum")
    for i in range(len(nums)):
        print(score, "score")
        print(nums)
        print(nums[i])
        if(nums[i] == minNum):
            score += nums[i]
            nums[i] = 0
            print(i, "i's value")
            
            if(i+1 in range(1,len(nums))):
               nums[i+1] = 0
            if(i-1 in range(1,len(nums))):
               nums[i-1] = 0
            break


print(nums)
print(score)
