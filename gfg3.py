arr = [1,2,3,4,5]
d = 2

def rev(start, end):
    while start <= end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


rev(0,d-1)
rev(d,len(arr)-1)
rev(0,len(arr)-1)


print(arr)


# arr = [2,1,5,4,3]


    
    




    
