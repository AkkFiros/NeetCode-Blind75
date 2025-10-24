"""
Longest Repeating Character Replacement
Link: https://neetcode.io/problems/longest-repeating-substring-with-replacement

Difficulty: Medium

Task:
You are given a string s consisting of only uppercase english characters and an integer k.
You can choose up to k characters of the string and replace them with any other uppercase English character.
After performing at most k replacements, return the length of the longest substring which contains only one distinct character.
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Given a string, returns the length of the longest possible substring that only contains 1 character,
        after up to k substitutions are made.

            Parameters:
                    s (str): a string
                    k (int): the maximum number of substitutions that can be made

            Returns:
                    int: the length of the longest substring within s that does only contains 1 character,
                         after up to k substitutions.
        """
        # left edge of sliding window
        left_ptr = 0

        # dictonary to keep track of characters and their frequencies in the window
        char_count = {}

        # longest chain of repeating characters in current window
        max_freq = 0

        res = 0

        for right_ptr in range(len(s)):
            # keep track of the frequency of unique characters in current window
            if s[right_ptr] not in char_count:
                char_count[s[right_ptr]] = 1
            else:
                char_count[s[right_ptr]] += 1

            max_freq = max(max_freq, char_count[s[right_ptr]])

            # check if current window is valid after accounting for replacements
            while (right_ptr - left_ptr + 1) - max_freq > k:
                char_count[s[left_ptr]] -= 1
                left_ptr += 1

        res = max(res, right_ptr - left_ptr + 1)

        return res