def canJump(self, nums) -> bool:
    n = len(nums)
    max_ind = 0
    for i in range(n):
        if i > max_ind:
            return False
        max_ind = max(max_ind , i+nums[i])
        if max_ind >= n-1:
            return True
    return False