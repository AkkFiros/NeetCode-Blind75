"""
Find Minimum in Rotated Sorted Array
Link: https://neetcode.io/problems/find-minimum-in-rotated-sorted-array

Difficulty: Medium

Task:
You are given an array of length n which was originally sorted in ascending order.
It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:
- [3,4,5,6,1,2] if it was rotated 4 times.
- [1,2,3,4,5,6] if it was rotated 6 times.

Notice that rotating the array 4 times moves the last four elements of the array to the beginning.
Rotating the array 6 times produces the original array.

Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?
"""

class Solution:
    def findMin(self, nums: list[int]) -> int:
        """
        Finds the minimum element in a given integer array nums, which has been rotated between 1 and n times.

            Parameters:
                    nums (lint[int]): a integer array that has been rotated
                                      for an unknown number of times, but at least once

            Returns:
                    int: the minimum element in nums
        """
        n = len(nums)
        
        left = 0
        right = n - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1

        return nums[left]

