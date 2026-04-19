class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        best = 1

        l = r = 0
        seen = defaultdict(int)

        while r < len(fruits):
            seen[fruits[r]] += 1
            if len(seen) <= 2:
                best = max(best, r - l + 1)
            else:
                seen[fruits[l]] -= 1
                if seen[fruits[l]] == 0:
                    del seen[fruits[l]]
                l += 1
            r += 1
        return best
