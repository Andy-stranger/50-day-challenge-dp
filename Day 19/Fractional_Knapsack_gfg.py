def fractionalknapsack(self, val, wt, capacity):
    arr = []
    for i in range(len(val)):
        arr.append([val[i],wt[i]])
    arr.sort(key = lambda x: (-x[0]/x[1]))
    res = 0
    cap = capacity
    for i in arr:
        if i[1] <= cap:
            res += i[0]
            cap -= i[1]
        else:
            res += i[0]*(cap/i[1])
            cap = 0
        if cap == 0:
            break
    return round(res,6)