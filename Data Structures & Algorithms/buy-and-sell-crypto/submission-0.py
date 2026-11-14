class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        min_so_far = prices[0]
        for price in prices:
            if price - min_so_far > best:
                best = price - min_so_far
            if price < min_so_far:
                min_so_far = price 
        return best
