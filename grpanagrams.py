def groupAnagrams(strs):
    res = {}
    N = len(strs)
    for i in range(N):
        curr = strs[i]
        if str(sorted(curr)) not in res.keys():
            res[str(sorted(curr))] = [curr]
            for j in range(i+1, N):
                if(sorted(curr) == sorted(strs[j])):
                    res[str(sorted(curr))].append(strs[j])

    print(res.values())

groupAnagrams(["act","pots","tops","cat","stop","hat"])
