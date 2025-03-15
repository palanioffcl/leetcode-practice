arr = [1]
maxval = max(arr)
total_sum = maxval*(maxval+1)//2
currsum = sum(arr)
        
if((total_sum - currsum) == 0):
    print(maxval + 1)
else:
    print(total_sum - currsum)
