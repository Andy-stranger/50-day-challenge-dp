def searchRange(self, nums, target: int):
    n = len(nums)
    lowerbound, upperbound = -1, -1
    
    left = 0
    right = n-1
    while left <= right:
        mid = left + (right - left)//2
        if nums[mid] >= target:
            lowerbound = mid
            right = mid - 1
        else:
            left = mid + 1
    
    left = 0
    right = n-1
    while left <= right:
        mid = left + (right - left)//2
        if nums[mid] <= target:
            upperbound = mid
            left = mid + 1
        else:
            right = mid - 1
    
    if lowerbound == -1 or upperbound == -1 or nums[lowerbound] != target:
        return [-1,-1]
    return [lowerbound,upperbound]