class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # var to keep track of longest valid string
        l = r = best = 0 

        # hash map to store seen characters
        seen = {}
        
        # until the right pointer goes out of bounds
        while r < len(s):
            if s[r] not in seen:
                seen[s[r]] = 1
                best = max(best, r - l + 1)
                r += 1
            else:
                seen.pop(s[l])
                l += 1

        # return var
        return best