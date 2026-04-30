class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = defaultdict(int)

        prefixSum[0] = 1

        runningSum = 0
        res = 0

        for num in nums:
            runningSum += num

            if runningSum - k in prefixSum:
                res += prefixSum[runningSum - k]

            prefixSum[runningSum] += 1

        return res