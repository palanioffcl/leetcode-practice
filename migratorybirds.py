arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]
dres = {}

for i in arr:
    if i not in dres.keys():
        dres[i] = 1
    else:
        dres[i] += 1


klist = list(dres.keys())
vlist = list(dres.values())

maxval = max(vlist)

pos = []
for i in range(len(vlist)):
    if vlist[i] == maxval:
        pos.append(klist[i])

print(min(pos))
