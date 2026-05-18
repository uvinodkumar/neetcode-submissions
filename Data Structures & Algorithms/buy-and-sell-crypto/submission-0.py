class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        left = 0

        max_profit = 0

        for right in range(1,n):

            if prices[right] - prices[left] < 0:
                left = right
            else:
                profit = prices[right] - prices[left]
                max_profit = max(profit, max_profit)
                right += 1
        
        return max_profit

        