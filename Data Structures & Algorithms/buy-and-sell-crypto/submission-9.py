class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = r = maxp = 0


        # for price in prices we need to pick a day to buy and a day to sell
        # left and right pointer

        while r < len(prices):
            if prices[r] > prices[l]:
                maxp = max(maxp, prices[r] - prices[l])
            else:
                l = r
            r += 1

        return maxp