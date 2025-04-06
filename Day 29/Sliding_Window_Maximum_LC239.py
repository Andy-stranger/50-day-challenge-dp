from collections import deque

def maxSlidingWindow(self, nums, k: int):
    n = len(nums)
    dq = deque()
    res = []
    for i in range(n):
        while dq and dq[-1] < nums[i]:
            dq.pop()
        dq.append(nums[i])
        if i >= k and nums[i-k] == dq[0]:
            dq.popleft()
        if i >= k-1:
            res.append(dq[0])
    return res