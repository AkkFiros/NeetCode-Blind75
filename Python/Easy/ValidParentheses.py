"""
Valid Parentheses
Link: https://neetcode.io/problems/validate-parentheses

Difficulty: Easy

Task:
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:
- Every open bracket is closed by the same type of close bracket.
- Open brackets are closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

Return true if s is a valid string, and false otherwise.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        """
        Checks if a given string of parentheses is valid.

            Parameters:
                    s (str): a string of parentheses

            Returns:
                    bool: True if s is valid, False otherwise
        """
        stack = []
        mapping = { ")": "(",
                    "}": "{",
                    "]": "[" }
        
        for char in s:
            if not stack:
                if char in mapping:
                    return False
                else:
                    stack.append(char)
            else:
                if char in mapping:
                    if stack[-1] == mapping[char]:
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(char)

        return not stack