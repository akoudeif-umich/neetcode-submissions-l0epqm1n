class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, best = -1, 0, 0
        seen = {}
        while r < len(s):
            # move right pointer until invalid 
            while r < len(s) and s[r] not in seen:
                seen[s[r]] = 1
                best = max(best, r - l)
                r += 1
            while r < len(s) and s[r] in seen:
                seen.pop(s[l + 1])
                l += 1
            
        return best
            
