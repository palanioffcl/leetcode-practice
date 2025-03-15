s = "cczazcc"
repeatLimit = 3

freq = {}

for i in s:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] += 1



klist = list(freq.keys())
vlist = list(freq.values())

counter = []

for i in range(len(klist)):
    counter.append(((-ord(klist[i]), vlist[i])))


heapq.heapify(counter)


res = []
                   
while counter:
    char, cnt = heapq.heappop(counter)
    char = chr(-char)
    currcnt = min(cnt, repeatLimit)
    res.append(char*currcnt)
    


    if(cnt - currcnt != 0 and counter):
        nxtchar, nxtcnt = heapq.heappop(counter)
        nxtchar = chr(-nxtchar)
        res.append(nxtchar)
        if nxtcnt != 0:
            heapq.heappush(counter, [-ord(nxtchar), nxtcnt-1])
        heapq.heappush(counter, [-ord(char), cnt - currcnt])
        


print("".join(res))
