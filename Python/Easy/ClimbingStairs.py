"""
Climbing Stairs
Link: https://neetcode.io/problems/climbing-stairs

Difficulty: Easy

Task:
You are given an integer n representing the number of steps to reach the top of a staircase.
You can climb with either 1 or 2 steps at a time.

Return the number of distinct ways to climb to the top of the staircase.
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Returns the number of ways to climb n steps if you take 1 or 2 steps each time.

            Parameters:
                    n (int): the number of steps to climb

            Returns:
                    int: the number of ways
        """
        if n <= 2:
            return n
        
        first = 1
        second = 2

        for i in range(3, n + 1):
            temp = first
            first = second
            second += temp

        return second