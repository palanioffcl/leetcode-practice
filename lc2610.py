nums = [1,3,4,1,2,3,1]
res = []

while nums:
    tmp = []
    cnt = 0
    while cnt != len(nums)-1:
        print(res, "RES")
        print(cnt)
        print(tmp,"tmp")
        print(nums)
        if nums[cnt] not in tmp:
            tmp.append(nums[cnt])
            nums.remove(nums[cnt])
            break
        cnt+=1
    res.append(tmp)
    print(res)
