def canAttendMeetings(intervals):
    if(len(intervals) != 0):
        sorted(intervals)
        start = intervals[0].start
        end = intervals[0].end
        
        for i in range(1, len(intervals)):
            if(intervals[i].start > start and intervals[i].end >end):
                start = intervals[i].start
                end = intervals[i].end
            else:
                return False
            
        return True
    else:
        return True


print(canAttendMeetings([(5, 10), (0,4) ]))
