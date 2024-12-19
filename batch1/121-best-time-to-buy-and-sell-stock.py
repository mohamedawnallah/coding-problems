class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_low, max_profit = prices[0], 0
        for price in prices:
            # We found local minimum
            if price < buy_low:
                buy_low = price
            else:
                max_profit = max(max_profit, price-buy_low)
        
        return max_profit
