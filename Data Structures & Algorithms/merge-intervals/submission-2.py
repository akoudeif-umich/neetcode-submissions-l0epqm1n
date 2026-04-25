class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals always come in pairs 
        # overlap logic: 
        # if end of interval A is >= Interval B start and <= B end

        # for list in intervals
            # store start end
            # temp list
            # for list + 1 in intervals
                # store start end
                # check overlap
                # update temp list
                # append temp list to res

        #return res 

        res = []
        # sort intervals 
        intervals.sort()

        # store the first start, end 
        prev_start, prev_end = intervals[0]

        # loop through list in intervals:
        for i in range(1, len(intervals)):
            # store curr start and end
            curr_start, curr_end = intervals[i]

            #check if overlap with prev
            # yes: merge
            if curr_start <= prev_end:
                prev_end = max(prev_end, curr_end)
            # no append prev and update
            else:
                res.append([prev_start, prev_end])
                prev_start, prev_end = curr_start, curr_end
        res.append([prev_start, prev_end])

        return res




