class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # obvious approach: loop through get 
        # the product and then loop through again and dived by each number

        n = len(nums)
        # Initialize three separate lists
        prefix = [0] * n
        sufix = [0] * n
        res = [0] * n

        # [1, 1, 2, 8]
        prefix[0] = sufix[len(nums) - 1] = 1
        for i in range(1, len(prefix)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        for i in range(len(sufix) - 2, -1, - 1):
            sufix[i] = sufix[i + 1] * nums[i + 1]
        
        for i in range(len(nums)):
            res[i] = prefix[i] * sufix[i]

        return res
            