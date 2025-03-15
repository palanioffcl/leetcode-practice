def isValid(s):
    x = list(s)
    stack = []
    for i in range(len(x)):
        if(x[i] in '{(['):
            stack.append(x[i])
        else:
            if(len(stack) == 0):
                break
            else:
                if(x[i] == '}' and stack[-1] == '['):
                    stack.remove('[')
                elif(x[i] == ')' and stack[-1] == '('):
                    stack.remove('(')
                elif(x[i] == ']' and stack[-1] == '['):
                    stack.remove('[')
                
    return True if len(stack) == 0 else False


print(isValid("]"))
