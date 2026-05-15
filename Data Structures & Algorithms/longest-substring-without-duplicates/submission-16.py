class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Brute force: 
        nested loop 

        single pass:
        set to keep track of what you have seen 

        best to keep track of best so far

        left pointer: 
            if right is in seen
            move left
            otherwise move right pointer check best
        """


        # left and right pointers
        l = r = 0

        # best var
        best = 0

        # seen set
        seen = set()

        # while r < len(s):
        while r < len(s):
            # if s[r] not in seen:
            if s[r] not in seen:
                # check best move right pointer
                best = max(best, r - l + 1)
                seen.add(s[r])
                r += 1

            # else:
            else: 
                # pop remove left pointer 
                seen.remove(s[l])
                # push forward 
                l += 1

        return best





