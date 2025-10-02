"""
Top K Frequent Elements
Link: https://neetcode.io/problems/top-k-elements-in-list

Difficulty: Medium

Task:
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.
"""

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        From an integer array, return the k-number of elements that appear the most

            Parameters:
                    nums (list[int]): an integer array
                    k (int): an integer

            Returns:
                    list[int]: an integer array containing k-number of unique elements from nums, that appear the most frequently
        """
        freq = {}
        buckets = [[] for i in range(len(nums) + 1)]
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        for kvp in freq.items():
            buckets[kvp[1]].append(kvp[0])
        
        output = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                output.append(num)
                if len(output) == k:
                    return output
    
"""
Notes:
- Bucket sort method above has O(n) time and space complexities.
- Sorting method below has O(n logn) time complexity and O(n) space complexity.
- Sorting method:
    class Solution:
        def topKFrequent(self, nums: list[int], k: int) -> list[int]:
            freq = {}
            for num in nums:
                if num in freq:
                    freq[num] += 1
                else:
                    freq[num] = 1
        
            char_sorted = sorted(freq.items(), key= lambda x:x[1], reverse= True)
        
            output = []
            for i in range(k):
                output.append(char_sorted[i][0])

            return output
"""