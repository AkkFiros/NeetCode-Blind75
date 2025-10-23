"""
Best Time to Buy and Sell Stock
Link: https://neetcode.io/problems/buy-and-sell-crypto

Difficulty: Easy

Task:
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Given the price of a coin across several days, returns the largest possible profit that can be made.

            Parameters:
                    prices (list[int]): the prices of a coin across several days (1 price per day)

            Returns:
                    int: the maximum profit that can be made
        """
        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            if price < min_price:
                min_price = price
            else:
                curr_profit = price - min_price
                max_profit = max(max_profit, curr_profit)

        return max_profit