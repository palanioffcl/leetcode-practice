arr = [10,10,10]
x = list(set(arr))
x.sort()
if(len(x) > 1):
    print(x)
else:
    print(-1)
