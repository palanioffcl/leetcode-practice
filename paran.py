def isValid(s):
    res = []
    if(len(s) <= 1):
        return False
    else:
        for i in s:
            if i in "{([":
                res.append(i)
            if(len(res) != 0):
                if(i == '}' and res[-1] == '{'):
                    res.pop()
                elif(i == ')' and res[-1] == '('):
                    res.pop()
                elif(i == ']' and res[-1] == '['):
                    res.pop()
            else:
                return False
    if(len(res) != 0):
        return False
    else:
        return True

print(res)
print(isValid("(])"))
