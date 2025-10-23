"""
Longest Substring Without Repeating Characters
Link: https://neetcode.io/problems/longest-substring-without-duplicates

Difficulty: Medium

Task:
Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Given a string, returns the length of the longest possible substrings that does not have any repeated characters.

            Parameters:
                    s (str): a string

            Returns:
                    int: the length of the longest substring within s that does not have any repeated characters
        """
        if not s:
            return 0
        
        left_ptr = 0

        # set to keep track of seen characters
        seen = set()

        max_len = 0

        for right_ptr in range(len(s)):
            while s[right_ptr] in seen:
                seen.remove(s[left_ptr])
                left_ptr += 1

            seen.add(s[right_ptr])
            max_len = max(max_len, right_ptr - left_ptr + 1)

        return max_len