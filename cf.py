for i in range(int(input())):
    x,y = input().split(' ')
    x = int(x)
    y = int(y)
    for j in range(min(x,y),1000000):
        if(j % x == j %y):
            print(j)
            break
