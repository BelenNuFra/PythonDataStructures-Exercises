"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order."""


class Solution(object):
    # Define the twoSum method which takes a list of numbers and a target sum.
    def twoSum(self, nums, target):
        # Initialize the index to start from the first element of the list.
        index = 0 
        # Initialize an empty list to store the indices of the two numbers that sum to the target.
        List = []
        
        # Iterate over the list until the second-to-last element (since we need to check pairs).
        while( index < len(nums) - 1 ): 
            # Calculate the difference between the target and the current number.
            subst = target - nums[index]
            
            # Check all the elements after the current number for a match.
            for i  in range(index + 1, len(nums)): 
                # If a matching number is found, append the indices to the list.
                if subst == nums[i]: 
                    List.append(index)
                    List.append(i)
                    # Return the list with the two indices.
                    return List
            # Increment the index to move to the next element.
            index += 1
