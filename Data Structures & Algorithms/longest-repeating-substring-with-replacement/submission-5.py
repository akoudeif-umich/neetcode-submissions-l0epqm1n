class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = best = mostf = 0

        count = defaultdict(int) # char : count

        while r < len(s):
            count[s[r]] += 1

            if count[s[r]] > mostf:
                mostf = count[s[r]]
            if r - l + 1 - mostf <= k:
                best = max(best, r - l + 1)
            else:
                count[s[l]] -= 1
                l += 1
            r += 1
        
        return best

