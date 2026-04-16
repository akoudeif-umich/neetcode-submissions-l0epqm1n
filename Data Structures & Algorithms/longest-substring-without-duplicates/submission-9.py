class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = best = r = 0
        seen = {}

        while r < len(s):
            if s[r] not in seen:
                seen[s[r]] = 1
                best = max(best, r - l + 1)
                r += 1
            else:
                seen.pop(s[l])
                l += 1
        return best
