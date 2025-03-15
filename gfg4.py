arr = [-2,0,10,-19,4,6,-8]
out = False
N = len(arr)

for i in range(N):
    for j in range(N):
        if(i != j and arr[i] == arr[j]*2):
            out = True
            break

print(out)
