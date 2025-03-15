import math
pi = str(format(math.pi, '.30f')).replace(".","")

res = []

for i in range(int(input())):
    s = input()
    cont = 0
    print(cont)
    for j in range(len(s)):
        if(j == len(s)):
            cont += 1
            res.append(cont)
        if(s[j] == pi[j]):
            cont += 1
        else:
            res.append(cont)
            

print(res)
