from itertools import product
def validStrings(n):
        data = list(map(''.join, product("01", repeat = n)))
        res = set()
        #for i in range(len(data)):
        #    if(data[i].count('1') >= n-1):
        #        res.add(data[i])
        #    else:                
        #        flag = True
        #       for j in range(n):
        #            for k in range(j+1,n):
        #                if(sorted(data[i][j:k+1]).count('1') < 1):
        #                    flag = False
        #                    break    
        #        if(flag == True):
        #            res.add(data[i])

        for i in data:
            if('00' not in i):
                res.add(i)
                
        return res

print(validStrings(18))
