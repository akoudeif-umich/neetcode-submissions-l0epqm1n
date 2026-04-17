class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = maxf = r = best = 0

        count = defaultdict(int)

        while r < len(s):
            count[s[r]] += 1

            if count[s[r]] > maxf:
                maxf = count[s[r]]

            if r - l + 1 - maxf <= k:
                best = max(best, r - l + 1)
            else:
                count[s[l]] -= 1
                l += 1

            r += 1
        return best