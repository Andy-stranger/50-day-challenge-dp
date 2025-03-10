from typing import List

def minCostClimbingStairs(self, cost: List[int]) -> int:
    n = len(cost)
    first = cost[0]
    second = cost[1]
    res = 0
    for i in range(2,n):
        res = cost[i] + min(first,second)
        first = second
        second = res
    return min(first,second)