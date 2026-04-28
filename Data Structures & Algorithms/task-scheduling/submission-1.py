class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # simulating time
        time = 0

        # build freq map
        counts = defaultdict(int)
        for task in tasks:
            counts[task] += 1

        # keep a max heap of most freq task 
        maxHeap = [-count for count in counts.values()]

        heapq.heapify(maxHeap)

        # build a queue for cooldowns 
        q = deque()

        # while heap or queue:
        while maxHeap or q:
            # time += 1
            time += 1

            # if the heap exists pop the top
            if maxHeap:
                # add 1 to the popped value
                curr = 1 + heapq.heappop(maxHeap)

                # if val is not 0
                if curr != 0:
                    # put it into the queue with cooldown time
                    q.append((curr, time + n))
            # if queue: 
            if q:
                # check if top item cooldown has ended 
                if q[0][1] == time:
                # pop queue and put item back into the heap 
                    heapq.heappush(maxHeap, q.popleft()[0])

        # return time
        return time