class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Binary search of log n
        middle value allows me to check which side is sorted 
        """

        # l and right pointers 
        l, r = 0, len(nums) - 1

        # while l <= r:
        while l <= r:
            # find middle 
            m = l + (r - l) // 2

            # if middle == target:
            if nums[m] == target:
                return m

            # if the left side is sorted:
            if nums[m] >= nums[l]:
                # if the target is in left side:
                if nums[l] <= target < nums[m]:
                    # move right pointer
                    r = m - 1
                # else:
                else:
                    # move left pointer
                    l = m + 1

            # else:
            else:
                # if target in right side:
                if nums[m] < target <= nums[r]:
                    # move left pointer
                    l = m + 1
                #else:
                else:
                    # move right pointer
                    r = m - 1
        
        # return -1
        return -1
