def canPartition(nums):
    summ = sum(nums)
    if summ&1 == 1:
        return False
    target = summ//2
    dp = [[-1]*(2*summ+1) for _ in range(len(nums)+1)]
    def isSubSetPresentWithSum(ind,cur):
        if ind == len(nums):
            return cur == target
        if dp[ind][cur] != -1:
            return dp[ind][cur] == 1
        take = isSubSetPresentWithSum(ind+1,cur+nums[ind])
        not_take = isSubSetPresentWithSum(ind+1,cur)
        if take or not_take:
            dp[ind][cur] = 1
        else:
            dp[ind][cur] = 0
        return dp[ind][cur] == 1
    return isSubSetPresentWithSum(0,0)