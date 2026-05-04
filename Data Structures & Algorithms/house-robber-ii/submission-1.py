class Solution:
    def rob_helper(self, nums):
        rob1 = rob2 = 0

        for house in nums:
            temp = max(house + rob1, rob2)

            rob1 = rob2
            rob2 = temp 
        return rob2
    def rob(self, nums: List[int]) -> int:
        # brute force: starting at 0 and one at 1 step by 2 and compare results

        # [1, 1, 100, 1, 10, 10000, 1000]

        # rob1 = 111
        # rob2 = 10101


        

        return max(nums[0], self.rob_helper(nums[1:]), self.rob_helper(nums[:-1]))
