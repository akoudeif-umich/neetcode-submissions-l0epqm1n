class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        tracker = defaultdict(int)
        i = 0
        for num in nums:
            if target - num in tracker:
                return [tracker[target - num], i]
            tracker[num] = i
            i += 1
