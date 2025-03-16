def findLongestChain(self, pairs) -> int:
    n = len(pairs)
    pairs.sort(key=lambda x: x[1])
    prev = [0]*(n+2)
    for ind in reversed(range(1,n+1)):
        cur = [0]*(n+2)
        for prev_ind in reversed(range(n+1)):
            cur[prev_ind] = prev[prev_ind]
            if prev_ind == 0 or pairs[prev_ind-1][1] < pairs[ind-1][0]:
                cur[prev_ind] = max(cur[prev_ind], 1 + prev[ind])
        prev = cur[:]
    return prev[0]