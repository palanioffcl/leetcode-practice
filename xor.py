nums = [3,4,5,6,7,8]

# nums = [5,1,6]

# nums = [1,3]

'''
XOR[1] = 1          0
XOR[3] = 3          1
XOR[1,3] = 2        0, 1


1+3+2 = 6
'''

totalSum = sum(nums)

x = 0
for i in nums:
    x ^= i
totalSum += x


if(len(nums) > 2):
    res = []    
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            totalSum += nums[i] ^ nums[j]
else:
    pass

print(totalSum)

