def findTargetSumWays(arr, target):
    res = 0
    total = sum(arr)
    dp = [[-1 for _ in range(2*total + 1)] for _ in range(len(arr)+1)]
    def count_comb(ind,summ):
        if ind == len(arr):
            if summ == target:
                return 1
            return 0
        if dp[ind][summ+total] != -1:
            return dp[ind][summ+total]
        pos = 0
        neg = 0
        pos = count_comb(ind+1,summ+arr[ind])
        neg = count_comb(ind+1,summ-arr[ind])
        dp[ind][summ+total] = pos + neg
        return dp[ind][summ+total]
    return count_comb(0,0)