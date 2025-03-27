def maxProfit(self, prices) -> int:
    max_profit = 0
    so_far_cheap = prices[0]
    n = len(prices)
    for i in range(n):
        if prices[i] < so_far_cheap:
            so_far_cheap = prices[i]
        max_profit = max(max_profit , prices[i] - so_far_cheap)
    return max_profit