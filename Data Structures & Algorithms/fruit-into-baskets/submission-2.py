class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        best = 1

        for i in range(len(fruits) - 1):
            seen = {}
            seen[fruits[i]] = 1
            for j in range(i + 1, len(fruits)):
                if fruits[j] not in seen:
                    seen[fruits[j]] = 1

                if len(seen) > 2:
                    best = max(best, j - i)
                    break
                else:
                    best = max(best, j - i + 1)
                

        
        return best