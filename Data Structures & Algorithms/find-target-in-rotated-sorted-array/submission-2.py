class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # log n time: some sort of binary search

        # use a binary search to see if we ever find the target, update result if so

        """
        guaranteed to be sorted in ascending order before rotation
        what does the middle value tell me? 

        case 1: odd array
        [3, 4, (5), 1, 2]
        [4, 5, (1), 2, 3]
        [3, 4, 5, (6), 7, 1, 2]
        [4, 5, 6, (7), 1, 2, 3]

        at least 1 half of the array is sorted

        case 2: should be the same

        Test: 
        [3, 4, 5, (6), 7, 1, 2]
        l = 0, r = 6
        m = 3

        [3, 4, 5, 6, 7, (1), 2]
        l = 4, r = 6
        m = 5

        [3, 4, 5, 6, (7), 1, 2]
        l = 4, r = 4
        m = 4
        """

        # set l and r pointers for window 
        l, r = 0, len(nums) - 1

        # while the l <= r:
        while l <= r:

            # set the m value
            m = l + (r - l) // 2

            # if value at m == target return m
            if nums[m] == target:
                return m

            # determine if the left or right half is sorted
            # right half is sorted
            if nums[m] < nums[l]:
                # check if the target is in the sorted half, yes: cut out unsorted; no: cut out sorted
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            # left half is sorted
            else:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
        return -1
