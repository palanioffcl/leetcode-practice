nums= [2,1,3,5,6]
k = 5
multiplier = 2


import heapq

clone = []
for i in range(len(nums)):
    clone.append(nums[i])

print(clone)


heapq.heapify(nums)

for i in range(k):
    popped = heapq.heappop(nums)
    clone[clone.index(popped)] *= multiplier
    print(popped)
    #heapq.heappush(nums, popped * multiplier)

print(clone)
