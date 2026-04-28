class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix_sum = defaultdict(int)

        prefix_sum[0] = 1

        total = res = 0

        for num in nums:
            total += num

            if total - k in prefix_sum:
                res += prefix_sum[total - k]

            prefix_sum[total] += 1
        
        return res
