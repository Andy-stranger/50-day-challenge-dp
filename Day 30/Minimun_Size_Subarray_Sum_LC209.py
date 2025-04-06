def minSubArrayLen(self, target: int, nums) -> int:
    min_len = float("inf")
    n = len(nums)
    left = 0
    right = 0
    cur_sum = 0
    while left <= right and right < n:
        cur_sum += nums[right]
        while cur_sum >= target and left <= right:
            min_len = min(min_len , right-left+1)
            cur_sum -= nums[left]
            left += 1
        right += 1
    return 0 if min_len == float("inf") else min_len