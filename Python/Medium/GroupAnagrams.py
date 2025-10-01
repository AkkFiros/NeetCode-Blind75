"""
Group Anagrams
Link: https://neetcode.io/problems/anagram-groups

Difficulty: Medium

Task:
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
"""

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        Groups elements of an array of strings, strs, based on if they are anagrams..

            Parameters:
                    strs (list[str]): an array of strings

            Returns:
                    list[list[int]]: an array of arrays, with each subarray containing elemens from strs that are anagrams of each other
        """
        freq_dict = {}
        alphabet_index = { 'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5,
                           'g' : 6, 'h' : 7, 'i' : 8, 'j' : 9, 'k' : 10, 'l' : 11,
                           'm' : 12, 'n' : 13, 'o' : 14, 'p' : 15, 'q' : 16, 'r' : 17,
                           's' : 18, 't' : 19, 'u' : 20, 'v' : 21, 'w' : 22, 'x' : 23, 'y' : 24, 'z' : 25 }

        for word in strs:
            char_freq = [0] * 26
            for char in word:
                char_freq[alphabet_index[char]] += 1
            
            freq_tuple = tuple(char_freq)

            if freq_tuple in freq_dict:
                freq_dict[freq_tuple].append(word)
            else:
                freq_dict[freq_tuple] = [word]

        return list(freq_dict.values())