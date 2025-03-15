def topKFrequent(nums,k):
    res = []
    tmp = {}
    for i in nums:
        if i not in tmp.keys():
            tmp[i] = 1
        else:
            tmp[i] += 1
        
    klist = list(tmp.keys())
    vlist = list(tmp.values())

    print(klist)
    print(vlist)
    for i in range(len(vlist)):
        if(vlist[i] <= k):
            res.append(klist[i])
    return res


print(topKFrequent([1,1,1,2,2,3], 2))
