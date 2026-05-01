class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # one approach loop through and get the total sum 
        # loop through again and store the total divided by num


        # build a left and right array where array[i] is the sum of nums[i]s left and right

        # loop through nums and append left[i] * right[i]

        n = len(nums)

        # res array
        res = [0] * n
        # left array 
        left = [0] * n
        # right array 
        right = [0] * n

        left[0] = 1
        right[n - 1] = 1

        # [1, 2, 4, 6]
        # [1, 1, 2, 8]
        # loop forward and build left array 
        for i in range(1, n):
            left[i] = nums[i - 1] * left[i - 1]

        # loop backward and build right array 
        for i in range(n - 2, -1, -1):
            right[i] = nums[i + 1] * right[i + 1]

        # loop and append prod of left and right array
        for i in range(n):
            res[i] = left[i] * right[i]

        # return res 
        return res

        # O(n) time and space complexity
