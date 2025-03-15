for i in range(int(input())):
    arrsize,k = map(int, input().split())
    arr = [int(x) for x in input().split()]
    #print(arr)
    res = 0
    for x in range(1,arrsize):
        for y in range(i+1,arrsize):
            curr = arr[x] - arr[y]
            if(curr != 0):
                if(abs(curr)%k != 0):
                    res = max(res, x)

    if(res != 0):
        print("YES")
        print(res)
    else:
        print("NO")
