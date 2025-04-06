def maxFrequency(self, nums, k: int) -> int:
    n = len(nums)
    nums.sort()
    left = 0
    right = 0
    max_freq = 1
    cur_sum = 0
    while right < n and left <= right:
        cur_sum += nums[right]
        while left <= right and (nums[right] * (right-left+1)) > cur_sum+k:
            cur_sum -= nums[left]
            left += 1
        max_freq = max(max_freq , right-left+1)
        right += 1
    return max_freq