"""
3Sum
Link: https://neetcode.io/problems/three-integer-sum

Difficulty: Medium

Task:
Given an integer array nums, return all the triplets
[nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0,
and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets.
You may return the output and the triplets in any order.
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        From an array of integers, return a list of all triplets that add up to 0.

            Parameters:
                    nums (list[int]): an integer array

            Returns:
                    list[list[int]]: an array of integer triplets, where the sum of each triplet is 0.
        """
        nums_sorted = sorted(nums)
        length = len(nums)

        output = []

        ind = 0
        while ind < length - 2:
            if ind > 0 and nums_sorted[ind] == nums_sorted[ind - 1]:
                ind += 1
                continue
            
            complement = 0 - nums_sorted[ind]

            left = ind + 1
            right = length - 1

            while left < right:
                curr_sum = nums_sorted[left] + nums_sorted[right]
                if curr_sum == complement:
                    valid_trio = [nums_sorted[ind], nums_sorted[left], nums_sorted[right]]
                    output.append(valid_trio)
                    
                    # settle updating to check for other valid trios for nums_sorted[ind]
                    # nested while loops to make sure repeat values are not rechecked
                    left += 1
                    right -= 1
                    while left < right and nums_sorted[left] == nums_sorted[left - 1]:
                        left += 1
                    while left < right and nums_sorted[right] == nums_sorted[right + 1]:
                        right -= 1
                
                elif curr_sum < complement:
                    left += 1
                    while left < right and nums_sorted[left] == nums_sorted[left - 1]:
                        left += 1

                elif curr_sum > complement:
                    right -= 1
                    while left < right and nums_sorted[right] == nums_sorted[right + 1]:
                        right -= 1

            ind += 1
        return output