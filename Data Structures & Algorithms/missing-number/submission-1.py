class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        count = 0

        nums.sort()
        for num in nums:
            if count != num: 
                return count
            count += 1

        return count