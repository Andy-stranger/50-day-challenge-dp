#Brute force
def sorted_squared(arr):
    n = len(arr)
    for i in range(n):
        arr[i] *= arr[i]
    arr.sort()
    return arr

#Optimized
def sorted_squared(arr):
    n = len(arr)
    res = [0]*n
    left = 0
    right = 0
    for i in range(n):
        if arr[i] >= 0:
            right = i
            break
    left = right - 1
    t = 0
    while left >= 0 and right < n:
        if arr[left]**2 < arr[right]**2:
            res[t] = arr[left]**2
            left -= 1
        else: 
            res[t] = arr[right]**2
            right += 1
        t += 1
    while left >= 0:
        res[t] = arr[left]**2
        left -= 1
        t += 1
    while right < n:
        res[t] = arr[right]**2
        right += 1
        t += 1
    return res
