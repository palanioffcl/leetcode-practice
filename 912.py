import heapq

l = [5,2,3,1]

clone = []
heapq.heapify(l)

while len(l) != 0:
    clone.append(heapq.heappop(l))

print(clone)

