class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        adj list 

        if a current path makes more than k stops then return

        Brute force: 
        use dfs to try everyt path from source to dest
        early break with invalid stops 
        check the best/cheapest path 

        greedy approach try to select the cheapest path
        when stops > k abort 
        dont revisit already visited nodes 
        if you cant get to dest return -1
        otherwise return the weight of the path you are on

        """

        # adj list 
        adj = defaultdict(list)
        for fr, to, price in flights:
            adj[fr].append((price, to))  

        # init heap 
        min_heap = [(0, 0, src)]

        # visited set 

        # dijkstras
        # while heap:
        while min_heap:
            # pop weight and node of top
            w1, stops, node = heapq.heappop(min_heap)

            # if target return weight 
            if node == dst:
                return w1

            # for nei push neighbors onto heap:
            if stops <= k:
                for w2, nei in adj[node]:
                    # push the total weight
                    heapq.heappush(min_heap, (w1 + w2, stops + 1, nei))
                
        
        return -1
                    

