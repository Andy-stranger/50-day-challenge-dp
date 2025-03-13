def longestCommonSubsequence(text1, text2):
    n1 = len(text1)
    n2 = len(text2)
    
    prev = [0]*(n2+1)
        
    for ind1 in reversed(range(n1)):
        cur = [0]*(n2+1)
        for ind2 in  reversed(range(n2)):
            if text1[ind1] == text2[ind2]:
                cur[ind2] = 1 + prev[ind2+1]
            else:
                cur[ind2] = max(prev[ind2],cur[ind2+1])
        prev = cur[:]
    
    return prev[0]