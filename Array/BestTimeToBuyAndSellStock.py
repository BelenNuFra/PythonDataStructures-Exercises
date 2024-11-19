"""You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 """
 
 
 class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize an empty stack to keep track of prices as we iterate.
        stack = []
        
        # Initialize profit to 0, as initially there's no profit.
        profit = 0 

        # Iterate through the prices in reverse order (from the last day to the first).
        for i in range(len(prices)-1, -1, -1): 
            # Current price on day 'i'.
            current = prices[i]
            
            # Remove all elements from the stack that are smaller than the current price,
            # since they can't give a profit if sold after the current price.
            while stack and current > stack[-1]:
                stack.pop()
            
            # If there is a price in the stack that results in a greater profit, update the profit.
            if stack and stack[-1] - current > profit: 
               profit = stack[-1] - current

            # If the stack is empty, append the current price (first price from the end).
            if not stack:  
                stack.append(current)
            # If the stack's last element is smaller than the current price, append it to the stack.
            elif stack[-1] < current:
                stack.append(current)
        
        # Return the maximum profit found.
        return profit 
