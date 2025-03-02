def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
    dp = [[0.0] * k for k in range(1,query_row+2)]
    cur = [poured]
    for r in range(query_row+1):
        nxt = [0.0] * (r+2)
        for c in range(r+1):
            if cur[c] >= 1:
                remain = (cur[c] - 1.0)/2.0
                nxt[c] += remain
                nxt[c+1] += remain
                cur[c] = 1
        if r != query_row:
            cur = nxt
    return cur[query_glass]