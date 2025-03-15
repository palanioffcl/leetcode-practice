for i in range(int(input())):
    a,b = map(int,input().split())
    res = []
    for j in range(a):
        res.append(input())
    print(res)
    out = 0

    for k in res:
        if(len(k) <= b and out < b):
            out += 1

    print(out)
            
        
