x = "[ ( )"

ip = x.split()
stack = []
print(ip)
for i in ip:
    if (i == "{" or i == "[" or i == "("):
        print(stack, "PUSH")    
        stack.append(i)
    else:
        if((i == "}" and "{" in stack)):
            stack.remove("{")
        elif ((i == ")" and "(" in stack)):
            stack.remove("(")
        elif ((i == "]" and "[" in stack)):
            stack.remove("[")
        


if(len(stack) == 0):
	print("True")
else:
	print("False")
