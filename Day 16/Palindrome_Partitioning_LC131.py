def partition(self, s: str):
    n = len(s)
    res = []

    dp = [[0]*n for _ in range(n)]
    for l in range(1,n+1):
        for i in range(n-l+1):
            j = i+l-1
            if i == j:
                dp[i][j] = True
            elif s[i] == s[j] and (j == i+1 or dp[i+1][j-1]):
                dp[i][j] = True
            else:
                dp[i][j] = False

    def recur(ind,cur_par):
        if ind > n-1:
            res.append(cur_par[:])
            return
        for i in range(ind,n):
            if dp[ind][i]:
                cur_par.append(s[ind:i+1])
                recur(ind+1,cur_par)
                cur_par.pop()
    
    recur(0,[])

    return res