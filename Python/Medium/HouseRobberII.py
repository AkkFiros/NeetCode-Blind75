"""
House Robber II
Link: https://neetcode.io/problems/house-robber-ii

Difficulty: Medium

Task:
You are given an integer array nums where nums[i] represents the amount of money the ith house has.
The houses are arranged in a circle, i.e. the first house and the last house are neighbors.

You are planning to rob money from the houses, but you cannot rob two adjacent houses 
because the security system will automatically alert the police if two adjacent houses were both broken into.

Return the maximum amount of money you can rob without alerting the police.
"""

class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        Returns the largest amount of money that can be taken from a ring of houses, without robbing from adjacent houses

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
        if n == 2:
            return max(nums[0], nums[1])
        
        def rob_row(nums):
            prev = 0
            prev2 = 0
            for num in nums:
                new_total = max(prev, prev2 + num)
                prev2 = prev
                prev = new_total
            return prev
        
        # case 1: 1st house is robbed <=> exclude last house, the rest form a row
        # case 2: last house is robbed <=> exclude first house, the rest form a row
        case_1 = rob_row(nums[:n - 1])
        case_2 = rob_row(nums[1:])

        return max(case_1, case_2)