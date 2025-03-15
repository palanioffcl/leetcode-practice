nums = [2,1,3,5,6]
k = 5
multiplier = 2


#nums = [1,2]
#k = 3
#multiplier = 4


for i in range(k):
    minval = nums.index(min(nums))
    #for j in range(len(nums)):
    #    if(nums[j] < nums[minval]):
    #        minval = j
    nums[minval] *= multiplier
               

        
print(nums)
