def findMinArrowShots(self, points) -> int:
    prev = 0
    n = len(points)
    points.sort(key = lambda a : a[1])
    total = 1
    for i in range(1,n):
        if points[i][0] > points[prev][1]:
            prev = i
            total += 1
    return total