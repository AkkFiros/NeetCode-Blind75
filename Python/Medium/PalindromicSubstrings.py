"""
Palindromic Substring
Link: https://neetcode.io/problems/palindromic-substrings

Difficulty: Medium

Task:
Given a string s, return the number of substrings within s that are palindromes.

A palindrome is a string that reads the same forward and backward.
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Returns the number of substrings within a string s, that are also palindromes.

            Parameters:
                    s (str): a string

            Returns:
                    int: the number of palindromic substring within s
        """
        n = len(s)
        if n == 0 or n == 1:
            return n
        
        def expand(left: int, right: int) -> int:
            count = 0
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1

            return count
        
        output = 0

        for i in range(n):
            odd_count = expand(i, i)
            even_count = expand(i, i + 1)
            output += odd_count + even_count

        return output