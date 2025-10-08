"""
Longest Consecutive Sequence
Link: https://neetcode.io/problems/longest-consecutive-sequence

Difficulty: Medium

Task:
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.
The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.
"""

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """
        From an integer array, nums, return the length of the longest consecutive integer sequence
        that can be formed.

            Parameters:
                    nums (list[int]): an integer array

            Returns:
                    int: the length of the longest consecutive integer sequence that can be formed from nums
        """
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        
        num_set = set(nums)
        checked = set()

        len_seq = 0

        for num in nums:
            if num in checked:
                continue
            else:
                checked.add(num)

            curr_add = num
            curr_sub = num
            count = 1
            while True:
                if curr_add + 1 in num_set:
                    count += 1
                    checked.add(curr_add + 1)
                    curr_add = curr_add + 1
                
                if curr_sub - 1 in num_set:
                    count += 1
                    checked.add(curr_sub - 1)
                    curr_sub = curr_sub - 1

                if curr_add + 1 not in num_set and curr_sub - 1 not in num_set:
                    break

            if count > len_seq:
                len_seq = count

        return len_seq
    
"""
Notes:
- Above is hybrid of "expand both sides" and "skip duplicates" methods
- Regardless of element, expand on either side of it and log into secondary tracker set
- If number appears in tracker set, then that number has been considered and you can skip it.
- Alternative "smallest element" method:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
- "smallest element" method determines the smallest possible element in a consecutive sequence
- if a smaller element exists, then skip it
- otherwise, expand rightwards (add) until no consecutive element exists
- both methods have O(n) time and space complexities
"""