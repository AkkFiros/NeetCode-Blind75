"""
Palindrome Number
Link: https://neetcode.io/problems/is-palindrome

Difficulty: Easy

Task:
Given astring s, return true if s is a palindrome, and false otherwise.
A palindrome is a string that reads the same forward and backward.
It is also case-insensitive and ignores all non-alphanumeric characters.
Note: s is length between 1 and 1000, inclusive.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Checks if a string is a palindrome, ignoring case and non-alphanumeric characters.

            Parameters:
                    s (str): a string

            Returns:
                    bool: True if x is a palindrome, False otherwise
        """

        # strip s of all non-alphanumeric characters, convert all to lowercase
        filtered_s = "".join(char.lower() for char in s if char.isalnum())

        len_s = len(filtered_s)

        # edge case: if s has only 1 chaaracter
        if len_s == 1:
            return True
        
        # initialise pointers
        pointer1 = 0
        pointer2 = len_s - 1

        while pointer2 > pointer1:
            char1 = filtered_s[pointer1]
            char2 = filtered_s[pointer2]

            if char1 != char2:
                return False
            
            pointer1 += 1
            pointer2 -= 1

        return True