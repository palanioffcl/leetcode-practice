#grid = [[3,2],[1,3],[3,4],[0,1]]
grid = [[3,2,1],[2,1,0],[1,2,3]]


'''
[3, 2]
[1, 3]
[3, 4]
[0, 1]
'''


res = 0
m = len(grid)
n = len(grid[0])


for i in range(n):
    for j in range(1,m):
        print(i,j)
        print(str(grid[j][i]) + "+" + str(grid[j-1][i]))
        if(grid[j][i] <= grid[j-1][i]):
            res += abs(grid[j][i] - grid[j-1][i])+1
            grid[j][i] = grid[j-1][i]+1

print(grid)
print(res)
