"""
Contains Duplicate
Link: https://neetcode.io/problems/duplicate-integer

Difficulty: Easy

Task:
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
"""

class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        """
        Checks if an integer array contains duplicate integers.

            Parameters:
                    nums (list[int]): an integer array

            Returns:
                    bool: True if there are duplicates in nums, False otherwise
        """

        appeared = set()

        for num in nums:
            if num in appeared:
                return True
            else:
                appeared.add(num)

        return False