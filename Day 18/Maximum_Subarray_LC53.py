def maxSubArray(nums):
    cur_sum = 0
    max_sum = float("-inf")
    for i in nums:
        cur_sum += i
        max_sum = max(max_sum,cur_sum)
        cur_sum = max(cur_sum,0)
    return max_sum