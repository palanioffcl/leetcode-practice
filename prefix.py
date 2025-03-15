strs = ["reflower","flow","flight"]
res = min(strs, key=len)
# print(res)
out = ""


for i in range(len(strs)):
    if(strs[i][0] != res[0]):
        print(out)



if(len(strs) == 1):
    #return strs
    print(strs[0])
else:
    for i in range(len(res)+1):
        tmp = res[:i]
        print(i)
        for j in range(len(strs)):
            if(strs[j][:i] == tmp):
                out = tmp


print(out)        
   # return out
