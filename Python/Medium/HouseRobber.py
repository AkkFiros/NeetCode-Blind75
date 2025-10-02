"""
House Robber
Link: https://neetcode.io/problems/house-robber

Difficulty: Medium

Task:
You are given an integer array nums where nums[i] represents the amount of money the ith house has.
The houses are arranged in a straight line, i.e. the ith house is the neighbor of the (i-1)th and (i+1)th house.

You are planning to rob money from the houses, but you cannot rob two adjacent houses 
because the security system will automatically alert the police if two adjacent houses were both broken into.

Return the maximum amount of money you can rob without alerting the police.
"""

class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        Returns the largest amount of money that can be taken from a row of houses, without robbing from adjacent houses

            Parameters:
                    nums (list[int]): an integer array, each element representing the amount of money held in a house

            Returns:
                    int: the largest amount of money that can be taken
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        memo = [0] * (n + 1)
        memo[1] = nums[0]
        
        for i in range(2, n + 1):
            # for this house, what is the max if I (1) skip it 
            # or (2) take it (together with the previous non-adjacent house)
            memo[i] = max(memo[i - 1], nums[i - 1] + memo[i - 2])

        return memo[n]