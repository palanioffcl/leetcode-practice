#arr = [1,2,3,4,5]
arr = [2 ,1 ,5 ,5 ,5 ,5 ,6 ,6 ,6 ,6 ,6]
N = len(arr)//3
x = list(set(arr))
res = {}

for i in x:
    res[i] = 0
    
for i in arr:
    res[i] += 1

print(len(arr))
print(sum(res.values()))
out = []
if(sum(res.values()) == len(arr)):
    print(out)
else:
    print(res, "RESS")
    for i in res.values():
        if(i >= N):
            out.append(list(res.keys())[list(res.values()).index(i)])

        
print(out)
