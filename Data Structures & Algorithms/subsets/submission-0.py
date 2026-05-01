class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Brute force:
        Input:
        [1,2,3]
             ^
        [[]]
        [[], [1]]
        [[], [1], [2], [1, 2]]
        [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

        # loop nums 

        # for each num create a subset of that number
        # check against prev subsets 
        # seen hash map

        """
        
        res = [[]]

        for num in nums:
            res += [subset + [num] for subset in res]

        return res

