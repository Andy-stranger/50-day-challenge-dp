def longestPalinSubseq(self, s):
    prev = [0 for _ in range(len(s))]
    for left in reversed(range(len(s))):
        curr = [0 for _ in range(len(s))]
        for right in range(left,len(s)):
            if left == right:
                curr[right] = 1
            elif s[left] == s[right]:
                curr[right] = prev[right-1] + 2
            else:
                curr[right] = max(curr[right-1],prev[right])
        prev = curr
    return prev[len(s)-1]