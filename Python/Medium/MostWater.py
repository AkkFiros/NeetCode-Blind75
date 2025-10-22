"""
Container With Most Water
Link: https://neetcode.io/problems/max-water-container

Difficulty: Medium

Task:
You are given an integer array heights where heights[i] represents the height of the i-th bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.
"""

class Solution:
    def maxArea(self, heights: list[int]) -> int:
        """
        Given an integer array of bars of varying heights, find the largest area of water that can be contained between 2 bars.
        (The width of the container is the distance between the 2 bars in the integer array.)

            Parameters:
                    heights (list[int]): an array of integers that represent the heights of bars

            Returns:
                    int: the largest area of water that can be contained between 2 bars.
        """
        left_ptr = 0
        right_ptr = len(heights) - 1
        max_area = 0

        while left_ptr < right_ptr:
            width = right_ptr - left_ptr
            height = min(heights[left_ptr], heights[right_ptr])
            curr_area = width * height
            max_area = max(max_area, curr_area)

            if heights[left_ptr] < heights[right_ptr]:
                left_ptr += 1
            else:
                right_ptr -= 1

        return max_area