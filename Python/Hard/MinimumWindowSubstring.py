"""
Minimum Window Substring
Link: https://neetcode.io/problems/minimum-window-with-characters

Difficulty: Hard

Task:
Given two strings s and t, return the shortest substring of s 
such that every character in t, including duplicates, is present in the substring.

If such a substring does not exist, return an empty string "".

You may assume that the correct output is always unique.
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Given 2 strings, s and t, returns the length of the shortest substring within s,
        that contains all characters in t.

            Parameters:
                    s (str): a string
                    t (str): a string

            Returns:
                    str: the shortest substring within s that contains all characters in t.
        """
        res = ""
        res_len = float("inf")

        # edge case: if t is longer than s, no valid results exist
        if len(t) > len(s) or t == "":
            return res
        
        # 1st dictionary to keep track of required characters in t
        t_chars = {}
        for char in t:
            if char not in t_chars:
                t_chars[char] = 1
            else:
                t_chars[char] += 1

        # need and have to track how many unique characters are required and how many are satisfied
        # reduces the need to repeatedly check dictionaries
        need = len(t_chars)
        have = 0

        left_ptr = 0
        window_chars = {}

        for right_ptr in range(len(s)):
            curr = s[right_ptr]
            
            if curr not in window_chars:
                window_chars[curr] = 1
            else:
                window_chars[curr] += 1

            if curr in t_chars and window_chars[curr] == t_chars[curr]:
                have += 1

            while have == need:
                # once all character requirements are satisfied,
                # shrink window to find minimum window
                if (right_ptr - left_ptr + 1) < res_len:
                    res_len = right_ptr - left_ptr + 1
                    res = s[left_ptr : right_ptr + 1]

                window_chars[s[left_ptr]] -= 1
                if s[left_ptr] in t_chars and window_chars[s[left_ptr]] < t_chars[s[left_ptr]]:
                    have -= 1

                left_ptr += 1

        return res