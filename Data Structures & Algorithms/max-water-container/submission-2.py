class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best, l, r = 0, 0, len(heights) - 1


        while l < r:
            if heights[l] < heights[r]:
                best = max(best, (r - l) * heights[l])
                l += 1
            else:
                best = max(best, (r - l) * heights[r])
                r  -= 1
        
        return best
            
        
