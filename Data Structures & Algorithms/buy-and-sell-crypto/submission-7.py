class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #prices[i] = neetcoin on the ith day 
        #choose a day to buy then sell in the future
        maxp = 0
        l , r = 0, 1

        while r < len(prices):
            maxp = max(maxp, prices[r] - prices[l])

            if prices[r] < prices[l]:
                l = r
            r += 1

        return maxp
