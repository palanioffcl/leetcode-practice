strs= ["eat","tea","tan","ate","nat","bat"]

res = set()
for i in range(len(strs)):
    tmp = []
    for j in range(i+1, len(strs)):
        if(sorted(strs[i]) == sorted(strs[j])):
            tmp.append(strs[j])
    res[strs[i]] = tmp

print(res)
