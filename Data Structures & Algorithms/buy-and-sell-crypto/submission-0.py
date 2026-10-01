class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        max_profit = 0 
        for i in range(len(prices)): 
            if prices[i] < min: 
                min = prices[i]
            curr = prices[i] - min 
            if curr > max_profit: 
                max_profit = curr 
        return max_profit 
            
