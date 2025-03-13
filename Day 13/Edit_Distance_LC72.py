def minDistance(word1, word2):
    n1 = len(word1)
    n2 = len(word2)
    
    prev = [0]*(n2+1)
        
    for ind2 in range(n2+1):
        prev[ind2] = n2 - ind2
        
    for ind1 in reversed(range(n1)):
        cur = [0]*(n2+1)
        cur[n2] = n1 - ind1
        for ind2 in reversed(range(n2)):
            if word1[ind1] == word2[ind2]:
                cur[ind2] = prev[ind2+1]
            else:
                cur[ind2] = 1 + min(cur[ind2+1] , prev[ind2] , prev[ind2+1])
        prev = cur[:]
    
    return prev[0]