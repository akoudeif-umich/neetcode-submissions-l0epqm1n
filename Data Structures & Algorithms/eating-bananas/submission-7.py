class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        best = r

        while l <= r:
            k = l + (r - l) // 2
            hours = 0
            for pile in piles:
                hours += (pile + k - 1) // k
                if hours > h:
                    break
            
            if hours > h:
                l = k + 1
            else:
                best = min(best, k)
                r = k - 1
        return best
