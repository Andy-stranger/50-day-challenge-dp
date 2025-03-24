def canCompleteCircuit(self, gas, cost) -> int:
    if sum(gas) < sum(cost):
        return -1
    total = 0
    res = 0
    n = len(gas)
    for i in range(n):
        total += gas[i] - cost[i]
        if total < 0:
            total = 0
            res = i+1
    return res