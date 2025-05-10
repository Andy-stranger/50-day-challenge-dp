def getLongestSubsequence(self, words, groups):
    res = [words[0]]
    n = len(words)
    prev = groups[0]
    for i in range(1,n):
        if groups[i] != prev:
            res.append(words[i])
            prev = groups[i]
    return res