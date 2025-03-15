s = "acc"

N = len(s)
res = {}


if(len(set(s)) == N):
    #return -1
    print(-1)
else:
    for i in range(N):
        for j in range(N):
            curr = s[i:j+1]
            if(len(set(curr)) == 1):            
                if (curr not in res.keys()):
                    res[curr] = 1
                else:
                    res[curr] += 1

klist = list(res.keys())
vlist = list(res.values())
ans = 0
out = ""

print(res)
for i in klist:
    if(len(i) > ans and res[i] >= 3):
        ans = len(i)
        out = i
#return ans

if(ans == 0):
    print(-1)
else:
    print(ans)
