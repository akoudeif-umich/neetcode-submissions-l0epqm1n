class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # need to track the frequency of elements as I loop through 
        # return k most freq elements 

        counts = defaultdict(int)
        heap = []

        for num in nums:
            counts[num] += 1

        for key, val in counts.items():
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for freq, num in heap]


        
            

