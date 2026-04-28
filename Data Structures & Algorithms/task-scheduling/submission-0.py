class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Input: 
        list of tasks where each tast is a char from 'A' - 'Z'

        if a task is identical then it must be seperated by n tasks

        can process one task per cpu cycle, 
        what is min number of cycles to complete tasks?


        """

        # get a count of how many times each letter appears
        counts = defaultdict(int)

        for task in tasks:
            counts[task] += 1

        # init time to zero 
        time = 0

        # build heap using counts each node can act as a char
        maxHeap = [-count for count in counts.values()]

        heapq.heapify(maxHeap)

        q = deque()

        # while the heap exists:
        while maxHeap or q:
            # increment time
            time += 1

            # pop the top task set it to -= 1
            if maxHeap:
                count = heapq.heappop(maxHeap) + 1
                if count != 0:
                    q.append((count, time + n))
                
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time

            # put the top task into a queue 

            # if queue and task at front cooldown passed put it back into heap




