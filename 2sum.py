arr = [5,6,5,7,7,8]
target = 13

l,r = 0, len(arr)-1


res = 0
while l<=r:
    print(arr[l] + arr[r], "L and R values")
    curr = l+r//2
    if(arr[curr] + arr[r] == target):
        res += 1
    elif(curr > target):
        r -= 1
    else:
        l += 1

print(res)
