class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        [2, 20, 4, 10, 3, 4, 5]
        ^

        keep track of best window so far 

        left and right pointers 

        when to update left pointer?
        when 
        """

        num_set = set(nums)
        best = 0

        for num in nums:
            if num - 1 not in num_set:
                length = 1
                while num + length in num_set:
                    length += 1
                best = max(length, best)
            
        return best
