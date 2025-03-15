3 - 5
'''
1 ** 3 **
2 * 232 *
3  12332
4 * 232 *
5 ** 3 **
'''

5 - 9
'''
1  **** 5 ****
2  *** 454 ***
3  ** 34543 **
4  * 2345432 *
5   123454321
6  * 2345432 *
7  ** 34543 **
8  *** 454 ***
9  **** 5 ****
'''


n = 3
x = n
n = n*2-1

for i in range(1,n+1):  
    if(i == 1 or i == n):
        x = ""
        for i in range(1,n+1):
            if(i == n-1):
                x += str(n)
            else:
                x += "*"
        print(x)
    else:
        y = ""
        if(i == x):
            for i in range(1,x):
                y += str(i)

            for i in range(x,0):
                y += str(i)
        print(y)
    else:
        z = ""
        for i in range(1,n+1):
            z += "*"
            
            
            
