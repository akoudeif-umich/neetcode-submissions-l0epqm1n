class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # what element appears the most 
        # if the sub string is a valid substring then is its length longer than current best
        # len(substring) - freq(most freq) <= k

        l = r = maxf = res = 0

        count = defaultdict(int)

        while r < len(s):
            count[s[r]] += 1
            if count[s[r]] > maxf:
                maxf = count[s[r]]

            if r - l + 1 - maxf <= k:
                res = max(res, r - l + 1)
            else:
                count[s[l]] -= 1
                l += 1
            r += 1
        return res 


