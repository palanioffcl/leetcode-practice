n = int(input())

for i in range(n):
    x = list(input())
    for i in range(len(x)):
        if(x[i] == 'p'):
            x[i] = 'q'
        elif(x[i] == 'q'):
            x[i] = 'p'
    print("".join(x[::-1]))
