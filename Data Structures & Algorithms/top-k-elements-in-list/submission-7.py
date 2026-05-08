class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        buckets =[[] for i in range(len(nums) + 1)]
        freq = defaultdict(int)
        res = []

        for num in nums:
            freq[num] += 1

        for num, f in freq.items():
            buckets[f].append(num)

        for i in range(len(nums), -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) >= k:
                    return res
