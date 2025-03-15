# i/p
s = "ababcbacadefegdehijhklij"
# o/p [9,7,8]

N = len(s)
res = {}

for i in range(N):
    if(s[i] not in res.keys()):
        res[i] = i
    else:
        res[i] = i

print(res)
