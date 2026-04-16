class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = best = 0
        seen = {}

        while r < len(s):
            # move right pointer until invalid
            while r < len(s) and s[r] not in seen:
                seen[s[r]] = 1
                best = max(best, r - l + 1)
                r += 1
            
            while r < len(s) and s[r] in seen:
                seen.pop(s[l])
                l += 1
        
        return best
        