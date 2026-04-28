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
        looping through a list of intervals count the number of overlapping intervals,
        unique intervals can all share a meeting room so starting min is 1

        Input:
        are the intervals sorted in any way or are they random?
        for each interval start < end 
        intervals are positive 

        Brute force:
        sort intervals based on start time 
        loop through and check if the prev end time is > curr start time
        time: O(n log n for sort)
        space: O(1) : in place sorting 

        ^
        brute force may actually be checking ever interval against all others for O(n^2)

        cant think of a better approach so I will start on this one
        """
        if not intervals:
            return 0

        intervals.sort(key=lambda obj : obj.start)
        
        heap = []

        heapq.heappush(heap, intervals[0].end)

        for i in range(1, len(intervals)):
            if intervals[i].start >= heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, intervals[i].end)
            else:
                heapq.heappush(heap, intervals[i].end)

        return len(heap)

        # need a way to know if a room freed up

        # maybe a heap 

        # top of heap = meeting most likely to be replaced

