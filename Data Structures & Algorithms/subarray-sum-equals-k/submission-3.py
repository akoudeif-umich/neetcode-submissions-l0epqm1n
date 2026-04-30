class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prev = defaultdict(int)

        res = total = 0

        prev[0] = 1


        for num in nums:
            total += num
            if total - k in prev:
                res += prev[total - k]
            
            prev[total] += 1

        return res
