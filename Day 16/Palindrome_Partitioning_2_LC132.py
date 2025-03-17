def minCut(self, s: str) -> int:
    n = len(s)

    isPalindrome = [[n+1]*n for _ in range(n)]
    for l in range(1,n+1):
        for i in range(n-l+1):
            j = i+l-1
            if i == j:
                isPalindrome[i][j] = True
            elif s[i] == s[j] and (j == i+1 or isPalindrome[i+1][j-1]):
                isPalindrome[i][j] = True
            else:
                isPalindrome[i][j] = False

    dp = [0]*n
    for end in range(n):
        minCut = end
        for start in range(end+1):
            if isPalindrome[start][end]:
                if start == 0:
                    minCut = 0
                else:
                    minCut = min(minCut,1+dp[start-1])
        dp[end] = minCut
        
    return dp[n-1]