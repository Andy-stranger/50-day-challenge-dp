def matrixMultiplication(self, arr):
    n = len(arr)
    dp = [[0]*n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0
    for i in reversed(range(1,n)):
        for j in range(i+1,n):
            cost = float("inf")
            for k in range(i,j):
                cur_cost = dp[i][k] + dp[k+1][j] + arr[i-1]*arr[k]*arr[j]
                cost = min(cost,cur_cost)
            dp[i][j] = cost
    return dp[1][n-1]
            
    # def recur(i,j):
    #     if i==j:
    #         return 0
    #     if dp[i][j] != -1:
    #         return dp[i][j]
    #     cost = float("inf")
    #     for k in range(i,j):
    #         cur_cost = recur(i,k) + recur(k+1,j) + arr[i-1]*arr[k]*arr[j]
    #         cost = min(cost,cur_cost)
    #     dp[i][j] = cost
    #     return dp[i][j]
    
    # return recur(1,n-1)