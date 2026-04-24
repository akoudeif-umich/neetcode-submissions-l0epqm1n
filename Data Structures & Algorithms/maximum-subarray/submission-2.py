class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        for i, num in enumerate(nums):
            if i - 1 >= 0:
                curr = nums[i - 1] + num
            else:
                curr = num
            
            if curr > num:
                nums[i] = curr

            best = max(best, nums[i])

        
        return best 


