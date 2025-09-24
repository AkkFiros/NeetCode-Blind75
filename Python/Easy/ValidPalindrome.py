"""
Palindrome Number
Link: https://neetcode.io/problems/is-palindrome

Difficulty: Easy

Task:
Given astring s, return true if s is a palindrome, and false otherwise.
A palindrome is a string that reads the same forward and backward.
It is also case-insensitive and ignores all non-alphanumeric characters.
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

