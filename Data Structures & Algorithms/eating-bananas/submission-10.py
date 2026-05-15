class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        [10, 20, 5, 15]

        h = 100000


        first find the max value in piles

        binary search 
        left mid right 

        if mid > h 
            check right of mid

        else:
            check if best 
            check left of mid 
        """

        # left and right pointers
        l, r = 1, max(piles)

        best = r


        # while l < r
        while l <= r:
            # set mid to r - l - 1
            mid = l + (r - l) // 2
            curr_h = 0

            # loop through piles and see if mid is valid
            for pile in piles:
                curr_h += -(-pile // mid)
                # if curr_h > h:
                if curr_h > h:
                    break
                    # break
            if curr_h > h:
                l = mid + 1
            # else: 
            else:
                #check best
                best = min(best, mid)
                # r = m - 1
                r = mid - 1

        return best







