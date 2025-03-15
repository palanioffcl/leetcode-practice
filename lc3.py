AllSubstrings = []
s ="ylfzmeipzgwsdzgrebwvshaelhsndxydifdxllmltifwkooqpmohtqngygudfshqzknlvbyrmfnwt"
maxLen = 1
if(len(s) == 0):
    print(0)
elif(len(s) == len(set(s))):
    print(len(s))
else:
    for i in range(len(s)):
        for j in range(i,len(s)):
            tmp = s[i:j+1]
            leng = len(tmp)
            x = ''.join(str(x) for x in set(tmp))
            if((x == tmp) and leng == len(set(tmp)) and maxLen < leng):
                    maxLen = len(tmp)
    print(maxLen)
