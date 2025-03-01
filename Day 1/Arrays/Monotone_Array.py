def isMonotonic(arr):
    n = len(arr)
    if n == 1 or n == 0:
        return True
    increasing = True
    decreasing = True
    for i in range(1,n):
        if arr[i] > arr[i-1]:
            decreasing = False
        if arr[i] < arr[i-1]:
            increasing = False
        if not increasing and not decreasing:
            return False
    return increasing or decreasing