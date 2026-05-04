class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        Input:
        n airports labeled 0 -> n-1
        array of flights [[from, to, price],...]
        no duplicate flights no self cylces
        Can a flight cost be negative? no 

        src = start point 
        dst = end point 
        src != dst 

        k is the max number of stops you can make along the way 

        return the cheapest flight from start to dst if it exits
        else return -1 

        weighted graph of flights 
        represent using an adjacency list

        some variation of dijkstras 
        greedily select the cheapest path as long as we are,
        within a valid number of stops
        """

        # adj list to represent the graph 
        adj = defaultdict(list)
        for start, to, price in flights:
            adj[start].append((to, price))

        # heap [(price, stops, airport)]
        heap = []
        heapq.heappush(heap, (0, 0, src))

        # while heap:
        while heap:
        # store and pop top of heap 
            curr_p, stops, curr = heapq.heappop(heap)

            # if target return cost
            if curr == dst:
                return curr_p

            # if within stops:
            if stops <= k:
                # for neighbors of node:
                for airport, price in adj[curr]:
                    # add price stop and airport for each neighbor to heap 
                    heapq.heappush(heap,(price + curr_p, stops + 1, airport))

        #return -1 
        return -1 



