def knapSack(n,W,val,wt):
    prev = [0]*(W+1)
    for _n in range(1,n+1):
        cur = [0]*(W+1)
        for _W in range(1,W+1):
            if wt[_n-1] > _W:
                cur[_W] = prev[_W]
            else:
                cur[_W] = max(
                            prev[_W],
                            val[_n-1]+cur[_W-wt[_n-1]]
                            )
        prev = cur[:]
    return prev[W]