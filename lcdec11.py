nums = [12,71]
k = 10

nums.sort()
l = 0
r = len(nums)

if(len(set(nums)) == 1):
    print(len(nums))
else:
    while (l <= r):
        mid = l+(r-l)//2
        print(mid)
        if(nums[mid] == 2*k):
            print(mid+1)
        if(nums[mid] < 2*k):
            r = mid-1
        else:
            l = mid+1

