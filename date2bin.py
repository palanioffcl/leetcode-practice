def convertDateToBinary(date):
    DateArray = date.split('-')
    res = []
    for i in DateArray:
        x = ""
        x += bin(int(i))[2:]
        res.append(x)
        
    return '-'.join(res)

print(convertDateToBinary("2080-02-29"))
