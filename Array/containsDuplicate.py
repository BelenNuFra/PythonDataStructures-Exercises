"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""


class Solution:
    # Function to check if a list contains any duplicate elements
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        dic = {}  # Initialize an empty dictionary to keep track of elements we have seen
        # Loop through each element in the input list 'nums'
        for i in range(len(nums)): 
            # Check if the current element already exists in the dictionary (i.e., it is a duplicate)
            if nums[i] in dic:
                return True  # If duplicate found, return True immediately
            else:
                dic[nums[i]] = nums[i]  # Otherwise, add the element to the dictionary
        return False  # If no duplicates are found, return False
