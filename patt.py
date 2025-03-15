'''
**3**
*232*
12321
*232*
**3**
'''

'''


****5****
***454***
**34543**
*2345432*
123454321
*2345432*
**34543**
***454***
****5****
'''

n = 5
for i in range(1,n+3):
    
    if(i == n):
        x = ""
        for i in range(1,n+1):
            x += str(i)
        for i in range(n-1,0,-1):
            x += str(i)
        print(x)
        
    elif(i%2 == 0):
        z = ""
        for i in range(1,n+3):
            if(i == n-1 or i == n+1):
                z += str(n-1)
            elif(i == n):
                z += str(n)
            else:
                z += "*"
        print(z)
    else:
        y = ""
        for j in range(n+2):
            if(j == n-1):
                y += str(n)
            else:
                y += "*"
        print(y)
    
