"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
        Input: list of intervals
        interval = [start, end] where start < end


        What causes a conflict?
        If a meeting exists with end > current start time
        
        Approach 1: order intervals by start time 

        loop through list check if prev end is > curr start 
        if so increment count
        """
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)

        heap = []

        heapq.heappush(heap, intervals[0].end)

        for i in range(1, len(intervals)):
            if intervals[i].start >= heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, intervals[i].end)
            else:
                heapq.heappush(heap, intervals[i].end)

        
        return len(heap)


