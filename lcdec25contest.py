#events = [[1,2],[2,5],[3,9],[1,15]]
#events = [[10,5],[1,7]]
#events = [[8,4],[7,6],[19,9],[8,14],[13,15],[2,16],[2,18]]
#events = [[9,4],[19,5],[2,8],[3,11],[2,15]]
events = [[1,4],[18,5],[15,7],[12,9],[1,11],[18,13],[16,17]]


maxPushTimeBtn = events[0][1]
maxPushTimeIndex = events[0][0]


for i in range(1,len(events)):
    Timediff = abs(events[i][1] - events[i-1][1])
    if(Timediff > maxPushTimeBtn):
        maxPushTimeBtn = events[i][1]
        maxPushTimeIndex = events[i][0]
    elif(Timediff == maxPushTimeBtn):
        if(events[i][0] < maxPushTimeIndex):
            maxPushTimeIndex = events[i][0]

print(maxPushTimeIndex)
