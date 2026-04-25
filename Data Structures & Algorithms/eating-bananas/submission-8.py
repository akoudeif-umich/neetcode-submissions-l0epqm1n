class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        brute force:
        test all values 1-k
        loop through container figure out how many hours it would take to,
        eat current index with current value of k
        the hours it takes is ceil(piles[i] / k) 

        so what is the max value of k?
        whatever the largest pile is

        use a binary search to find the value of k? 
        """

        
        # range of possible k : 1 - k

        l, r = 1, max(piles)
        best = r

        while l <= r:
            k = l + (r - l) // 2
            curr_h = 0

            for pile in piles:
                curr_h += (pile + k - 1) // k
                if curr_h > h:
                    break
            
            if curr_h > h:
                l = k + 1
            else:
                best = min(best, k)
                r = k - 1

        return best
        





