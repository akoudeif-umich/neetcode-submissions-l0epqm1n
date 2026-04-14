class Solution:
    def maxArea(self, heights: List[int]) -> int:
     
        best, l, r = 0, 0, len(heights) - 1

        while l < r:
            best = max(best, min(heights[r], heights[l]) * (r - l))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return best
