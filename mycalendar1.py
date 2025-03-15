events = [[0,0]]

inputt = [[10,20],[15,25],[20,30]]

for i in inputt:
    for start,end in events:
        print(start, end, "hii")
        if i[0] > start and i[1] < end:
            events.append("False")
        else:
            events.append("True")

print(events)
