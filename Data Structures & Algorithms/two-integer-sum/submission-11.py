class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # find two numbers in our list that sum to target
        # return indices in order 

        """
        loop through each item in list 
        loop through every other item and check if they sum to target


        optimal approach: 
        can I store the values as a go along?
        use a dictionary 
        """

        seen = {}

        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], i]
            seen[num] = i
            
