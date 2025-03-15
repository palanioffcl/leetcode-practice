x = [1,0,1]
for i in x:
    tmp = i
    x.remove(i)
    # print(x)
    # print(tmp,"TMP")
    if(tmp in x):
            pass
    else:
        print(tmp)
        break

