"""
Encode and Decode Strings
Link: https://neetcode.io/problems/string-encode-and-decode

Difficulty: Medium

Task:
Design an algorithm to encode a list of strings to a single string.
The encoded string is then decoded back to the original list of strings.
Please implement encode and decode
"""

class Solution:

    def encode(self, strs: list[str]) -> str:
        """
        Encode the elements of an array of strings, strs, into a single string.

            Parameters:
                    strs (list[str]): an array of strings

            Returns:
                    str: a string consisting of elements of strs
        """
        output = ""
        for elmnt in strs:
            prefix = str(len(elmnt)) + "#"
            output = output + prefix + elmnt

        return output

    def decode(self, s: str) -> list[str]:
        """
        Decode a string s, into individual strings that made up the original array of strings before encoding.

            Parameters:
                    s (str): a string

            Returns:
                    list[str]: an array of strings which were decoded from s
        """
        ind = 0
        res = []
        while ind < len(s):
            pointer = ind

            while s[pointer] != "#":
                pointer += 1

            len_elmnt = int(s[ind: pointer])
            ind = pointer + 1
            pointer = ind + len_elmnt

            elmnt = s[ind: pointer]
            res.append(elmnt)
            
            ind = pointer

        return res