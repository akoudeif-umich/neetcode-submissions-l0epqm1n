class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Input:
        nums of length n + 1

        each num in nums is (1 - n)

        seen = {}

        loop through nums:
            if num is already in seen then return that num

        O(n) time and space 
        

        if you want to optimize for space:
            brute force:
            a nested loop to check if you run into a number again


        [-1, -3, -4, -5, -2, 2]
                             ^            
        """

        # loop through nums:
        for i, num in enumerate(nums):
            # check the index of current num
            # if - then return current num:
            if nums[abs(nums[i]) - 1] < 0:
                return abs(num)
            # else:
            else:
                # mark index (num) as -
                nums[abs(nums[i]) - 1] *= -1
        

