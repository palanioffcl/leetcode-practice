strs = ["eat","tea","tan","ate","nat","bat"]
res = {}
for i in strs:
    if i not in res.keys():
        res[i] = [i]
    else:
        if(sorted(res[i])
        res[sorted(i)].append(i)
print(res.values())
print(list(res.values()))
