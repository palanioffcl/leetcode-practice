arr = [2,3,5,6]
k = 2

missing = []

for i in range(1,max(arr)):
    if i not in arr:
        missing.append(i)

print(missing)

if k <= len(missing):
    #return missing[k-1]
    print(missing[k-1])
else:
    #return max(arr) + (k - len(missing))
    print(max(arr) + (k - len(missing)))
