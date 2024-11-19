"""You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?"""

class Solution:
    # Function to compute the number of ways to climb 'n' stairs
    def climbStairs(self, n: int) -> int:
        # Base case: if there is only 1 step, there's only one way to climb (1 step)
        if n == 1:
            return 1
        # Base case: if there are 2 steps, there are two ways to climb (1 step + 1 step or 2 steps)
        elif n == 2:
            return 2
        
        # Initialize variables for the last two values in the sequence
        prev1, prev2 = 2, 1
        # Iterate from step 3 to 'n' to calculate the total ways
        for i in range(3, n + 1):
            # Current number of ways to reach the current step is the sum of the previous two
            current = prev1 + prev2
            # Update prev2 to be the previous prev1 (the previous step)
            prev2 = prev1
            # Update prev1 to be the current value (the number of ways to reach the current step)
            prev1 = current
        
        # Return the final result which is the number of ways to reach the 'n'th step
        return prev1
