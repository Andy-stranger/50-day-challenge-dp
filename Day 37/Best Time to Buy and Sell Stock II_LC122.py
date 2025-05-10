def maxProfit(prices):
    prev = []
    for i in reversed(range(len(prices))):
        for j in range(2):
            if j==1:
                buy = -prices[i] + prev[0]
                not_buy = prev[1]
                prev[j] = max(buy, not_buy)
            else:
                sell = prices[i] + prev[1]
                not_sell = prev[0]
                prev[j] = max(sell, not_sell)
    return prev[1];