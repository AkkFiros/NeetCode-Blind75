"""
Valid Anagram
Link: https://neetcode.io/problems/is-anagram

Difficulty: Easy

Task:
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Checks 2 strings are anagrams of each other.

            Parameters:
                    s (str): a string
                    t (str): a string

            Returns:
                    bool: True if s and t are anagrams of each other, False otherwise
        """

        len_s = len(s)
        len_t = len(t)

        if len_s != len_t:
            return False
        
        char_freq = {}
        for char in s:
            if char in char_freq:
                char_freq[char] += 1
            else:
                char_freq[char] = 1

        for char in t:
            if char not in char_freq:
                return False
            else:
                char_freq[char] -= 1
                if char_freq[char] < 0:
                    return False
                
        return True