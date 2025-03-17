def wordBreak(self, s: str, wordDict) -> bool:
    n = len(s)
    dp = [0]*(n+1)
    dp[0] = True

    for ind in range(1,n+1):
        for wrd in wordDict:
            if s[ind-len(wrd):ind] == wrd and dp[ind-len(wrd)]:
                dp[ind] = True
        if dp[ind] != True: 
            dp[ind] = False
    
    return dp[n]