class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = best = 0

        seen = {}

        while r < len(s):
            if s[r] not in seen:
                best = max(best, r - l + 1)
                seen[s[r]] = 1
                r +=1
            else:
                seen.pop(s[l])
                l += 1

        return best 