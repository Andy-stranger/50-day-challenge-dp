def minJumps(arr):
    n = len(arr)
    jump = 0
    cur_reach = 0
    max_reach = 0
    
    for i in range(n):
        max_reach = max(max_reach, i+arr[i])
        if max_reach >= n-1:
            return jump + 1
        if i == cur_reach:
            if i == max_reach:
                return -1
            else:
                jump += 1
                cur_reach = max_reach
    return -1