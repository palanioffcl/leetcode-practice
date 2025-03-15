s = "LeetcodeHelpsMeLearn"
spaces = [8,13,15]

res = []
res.append(s[:spaces[0]])
for i in range(1,len(spaces)):
    res.append(s[spaces[i-1]:spaces[i]])
    
res.append(s[spaces[-1]:])

return " ".join(res)
