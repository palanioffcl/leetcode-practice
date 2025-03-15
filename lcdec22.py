#nums = [1,2,3,4,2,3,3,5,7]
#nums = [4,5,6,4,4]
nums = [3,7,7,3]

if(nums == list(dict.fromkeys(nums))):
    print(0)
else:
    if(len(nums) <= 3 and nums != list(dict.fromkeys(nums))):
        print(1)
    elif(len(nums) <= 3 and nums == list(dict.fromkeys(nums))):
        print(1)
    else:
        res = 0
        while (nums != list(dict.fromkeys(nums))):
            nums = nums[3:]
            res += 1
        print(res)
