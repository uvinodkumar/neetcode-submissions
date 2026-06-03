class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0
        # profit = 0
        maxprofit = 0

        for right in range(1, len(prices)):


            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxprofit = max(profit, maxprofit)

            if prices[left] > prices[right]:
                left = right

        return maxprofit
