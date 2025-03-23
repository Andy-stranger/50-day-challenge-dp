def twoCitySchedCost(self, costs) -> int:
    n = len(costs)
    costs.sort(key = lambda a : a[0]-a[1])
    res = 0
    res += sum([costs[a][0] for a in range((n//2))])
    res += sum([costs[a][1] for a in range((n//2),n)])
    return res

    #Recursive dp (/memoization/tabulation) solution
    # n = len(costs)
    # def recur(ind,a):
    #     if ind == n:
    #         return 0
    #     costA = float("inf")
    #     if a < n//2:
    #         costA = costs[ind][0] + recur(ind+1,a+1)
    #     costB = float("inf")
    #     if ind-a < n//2:
    #         costB = costs[ind][1] + recur(ind+1,a)
    #     return min(costA,costB)
    # return recur(0,0)