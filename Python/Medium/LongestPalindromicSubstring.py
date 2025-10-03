"""
Longest Palindromic Substring
Link: https://neetcode.io/problems/longest-palindromic-substring

Difficulty: Medium

Task:
Given a string s, return the longest substring of s that is a palindrome.

A palindrome is a string that reads the same forward and backward.

If there are multiple palindromic substrings that have the same length, return any one of them.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Returns the longest substring of a string s, that is also a palindrome.

            Parameters:
                    s (str): a string

            Returns:
                    str: the longest palindromic substring within s
        """
        n = len(s)
        if n == 0:
            return ""
        
        def expand(left: int, right: int) -> tuple[int, int]:
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1

            return left + 1, right - 1
        
        # start and end indices of longest palindrome
        start = 0
        end = 0

        for i in range(n):
            odd_left, odd_right = expand(i, i)
            even_left, even_right = expand(i, i + 1)

            if odd_right - odd_left >= end - start:
                start = odd_left
                end = odd_right
            
            if even_right - even_left >= end - start:
                start = even_left
                end = even_right

        return s[start:end + 1]