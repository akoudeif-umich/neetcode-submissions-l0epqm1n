class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # keep track of the best so far
        best = 0

        # left and right pointers
        l = r = 0

        # keep track of what chars are in current window 
        seen = {}

        # while the r < len(s):
        while r < len(s):
            # if r is not in seen:
            if s[r] not in seen:
                # check best length
                best = max(best, r - l + 1)
                seen[s[r]] = 1
                # increment r 
                r += 1
            else:
                # remove l from seen and increment our left
                seen.pop(s[l])
                l += 1

        # return best
        return best


