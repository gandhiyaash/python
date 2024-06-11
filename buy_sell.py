'''
Leetcode : 122
Problem Statemet : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
'''

from typing import List

# Using greedy approach
def maxProfit(prices: List[int]):
    buy = prices[0]
    profit = 0
    for price in prices[1:]:
        if buy < price:
            profit += price - buy
        buy = price
    return profit


prices = [1,2,3,4,5]
result = maxProfit(prices)
print(result)


