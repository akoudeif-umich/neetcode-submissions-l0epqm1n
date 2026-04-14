class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        best = 0

        for l in range(0, len(heights) - 1):
            for r in range(l + 1, len(heights)):
                best = max(best, min(heights[r], heights[l]) * (r - l))
        return best