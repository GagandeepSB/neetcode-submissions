class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # left = buy, right = sell
        maxP = 0
        
        while r < len(prices):
            # Check if this is a profitable transaction
            # Calculate profit 
            # Check if this transaction is max profit
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(profit, maxP)

            # Might not be a profitable transaction
            # Set left ptr to right ptr since right ptr is a lower price than the left ptr
            else:
                l = r
            # Regardless of conditions, want to increment right pointer
            r += 1
        return maxP