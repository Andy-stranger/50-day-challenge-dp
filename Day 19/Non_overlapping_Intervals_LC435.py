def eraseOverlapIntervals(self, intervals) -> int:
    prev = 0
    count = 0
    intervals.sort(key = lambda a : a[1])
    for i in range(1,len(intervals)):
        if intervals[i][0] < intervals[prev][1]:
            count += 1
        else:
            prev = i
    return count