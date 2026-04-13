class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = prices[0]
        profit = 0

        for price in prices:
            minp = min(price, minp)
            profit = max(profit, price - minp)

        return profit
        