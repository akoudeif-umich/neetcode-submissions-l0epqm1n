class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = best = 0
        r = 1

        while r < len(prices):

            best = max(best, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r

            r += 1

        return best