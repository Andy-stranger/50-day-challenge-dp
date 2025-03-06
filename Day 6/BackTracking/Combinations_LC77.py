def combine(n: int, k: int):
    res = []
    def recur(curr,ind):
        if len(curr) == k:
            res.append(curr[:])
            return
        nd = k - len(curr)
        for i in range(ind,n-nd+2):
            curr.append(i)
            recur(curr,i+1)
            curr.pop()
        return
    recur([],1)
    return res