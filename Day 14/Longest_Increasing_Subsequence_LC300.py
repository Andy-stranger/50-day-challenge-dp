def lengthOfLIS(nums):
    n = len(nums)
    prev = [0]*(n+2)
    for ind in reversed(range(1,n+1)):
        cur = [0]*(n+2)
        for prev_ind in reversed(range(n+1)):
            cur[prev_ind] = prev[prev_ind]
            if prev_ind == 0 or nums[ind-1] > nums[prev_ind-1]:
                cur[prev_ind] = max(cur[prev_ind],1+prev[ind])
        prev = cur[:]
    return prev[0]