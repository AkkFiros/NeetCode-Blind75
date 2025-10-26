"""
Search in Rotated Sorted Array
Link: https://neetcode.io/problems/find-target-in-rotated-sorted-array

Difficulty: Medium

Task:
You are given an array of length n which was originally sorted in ascending order.
It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:
- [3,4,5,6,1,2] if it was rotated 4 times.
- [1,2,3,4,5,6] if it was rotated 6 times.

Given the rotated sorted array nums and an integer target,
return the index of target within nums, or -1 if it is not present.

You may assume all elements in the sorted rotated array nums are unique,

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?
"""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        Finds a specific element in a given integer array nums, which has been rotated between 1 and n times.

            Parameters:
                    nums (lint[int]): a integer array that has been rotated
                                      for an unknown number of times, but at least once
                    target (int): the element to be searched for in nums

            Returns:
                    int: the minimum element in nums
        """
        n = len(nums)

        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1