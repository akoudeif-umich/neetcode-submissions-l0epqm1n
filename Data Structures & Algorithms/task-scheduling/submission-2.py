class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0

        freq = defaultdict(int)

        for task in tasks:
            freq[task] += 1

        heap = [-f for f in freq.values()]

        heapq.heapify(heap)

        q = deque()

        while heap or q:
            time += 1

            if heap:
                curr = 1 + heapq.heappop(heap)

                if curr != 0:
                    q.append((curr, time + n))

            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])


        return time