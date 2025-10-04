"""
Products of Array Except Self
Link: https://neetcode.io/problems/products-of-array-discluding-self

Difficulty: Medium

Task:
Given an integer array nums, return an array output where output[i]
is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n) time without using the division operation?
"""

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
        From an integer array, nums, return an integer array, output,
        where each element is the product of elements in nums except nums[i]

            Parameters:
                    nums (list[int]): an integer array

            Returns:
                    list[int]: an integer array where the i-th element is 
                               the product of all elements in nums except nums[i]
        """
        output = [1] * len(nums)

        prefix = nums[0]
        for i in range(1, len(nums)):
            output[i] = prefix
            prefix *= nums[i]

        postfix = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]

        return output