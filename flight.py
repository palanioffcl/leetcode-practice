bookings = [[1,2,10],[2,3,20],[2,5,25]]
n = 5
res = [0]*(n+1)
for i in range(len(bookings)):
    print(bookings[i])
    for j in range(bookings[i][0], bookings[i][1]+1):
        print(j,"J value")
        res[j] += bookings[i][2]
    print(res)

print(res[1:])
