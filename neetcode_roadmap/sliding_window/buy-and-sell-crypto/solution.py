class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0 # Initialize max profit to 0
        for i in range(len(prices)): # Iterate through prices
            price = prices[i] # Get the price of the current day
            for j in range(i): # Iterate through the prices before the current day
                if price - prices[j] > max_profit: # If the profit is greater than the max profit
                    max_profit = price - prices[j] # Update the max profit
        return max_profit # Return the max profit
