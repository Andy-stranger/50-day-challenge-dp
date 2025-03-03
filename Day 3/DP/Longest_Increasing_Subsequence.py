def lis(self, arr):
    res = [arr[0]]
    for i in range(1,len(arr)):
        if res[-1] < arr[i]:
            res.append(arr[i])
        else:
            low = 0
            high = len(res)-1
            while low < high:
                mid = low + (high-low)//2
                if res[mid] < arr[i]:
                    low = mid+1
                else:
                    high = mid
            res[low] = arr[i]
    return len(res)