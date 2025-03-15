#ip = "(1 and 2 or (3 and 4) or 5"
ip = "(1 and 2 and 3 or 4 )"
res = "("

ip = " ".join(ip).split(' ')
print(len(ip))

for i in range(len(ip)):
    try:
        if(ip[i] == '' and ip[i+1] == ''):
            ip.pop(i)
    except:
        pass
print(ip)
for i in range(len(ip)):
    if(ip[i] == ''):
        pass
    else:
        res += ip[i]
        if(ip[i] == 'a' and ip[i+2] == 'd'):
            ip[i-1] = ip[i-2]
            ip[i-2] = '('
            ip[i+3] = ip[i+4]
            ip[i+4] = ')'
        #elif(ip[i] == 'o' and ip[i+1] == 'r'):
        #    ip[i-1] = ip[i-2]
        #    ip[i-2] = '('
        #    ip[i+3] = ip[i+4]
        #    if(ip[i+4].isnumeric()):
        #        ip[i+4] = 

         #ip[i+4] = ')'
res += ')'          
print(res)
