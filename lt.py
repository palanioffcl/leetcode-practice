def makeFancyString(s):
    ipstr = list(s)
    for i in range(len(ipstr)):
        print(i)
        print(len(ipstr))
        if(i == len(ipstr)):
            break
        elif(ipstr[i+1] != ipstr[i]):
            pass
        elif(ipstr[i+1] != ipstr[i+2]):
            pass
        else:
            ipstr.pop(i)
    
    return "".join(ipstr)

print(makeFancyString("leeetcodeee"))
