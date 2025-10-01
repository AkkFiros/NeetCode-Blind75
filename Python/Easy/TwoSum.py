"""
Two Sum
Link: https://neetcode.io/problems/two-integer-sum

Difficulty: Easy

Task:
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

**You may assume that every input has exactly one pair of indices i and j that satisfy the condition.**

Return the answer with the smaller index first.
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Returns the indices of 2 integers within an integer array nums that add up to target

            Parameters:
                    nums (list[int]): an integer array

            Returns:
                    list[int]: The indices of 2 integers within nums that add to target
        """

        mapping = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in mapping:
                return [mapping[complement], i]
            mapping[nums[i]] = i