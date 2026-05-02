class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        top k makes me think hea/pq

        freq map to determine frequency 

        store (freq, num) in a max heap 
        pop k elements in the heap 

        or a min heap and pop until there is only k elements in heap

        # time complexity: O(n log n)
        # space complexity: O(n)

        bucket sort:

        Build out frequency map 

        bucket array of length len(nums) + 1

        loop through freq map and put items into buckets

        loop backwards through buckets and append k elements to res

        time: O(n)
        space: O(n)
        """

        # res list
        res = []

        # buckets len(nums) + 1
        buckets = [[] for i in range(len(nums) + 1)]

        # freq map
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        # loop through freq map add to buckets
        for num, fre in freq.items():
            buckets[fre].append(num)
        


        # loop backwards through buckets 
        for i in range(len(buckets) - 1, -1, -1):
            # add to res
            for item in buckets[i]:
                res.append(item)
            # if len(res) == k:
                if len(res) == k:
                    return res
                # return res
        
        # return -1









