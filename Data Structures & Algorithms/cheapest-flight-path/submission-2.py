class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        Directed graph
        adj matrix

        Dijkstras algorithim 
        O(v * k log e * k)

        need to track stops 

        belleman fords algorithim 

        v - 1
        cheapest path after k + 1 
        check the best path to each node up to k + 1 times 

        """

        # build adj list
        adj = defaultdict(list)

        for s, d, p in flights:
            adj[s].append((d, p))

        # array to keep track of cheapest for each node
        res = [float("inf")] * n

        # init starting flight 
        res[src] = 0

        # loop k + 1 times:
        for i in range(k + 1):
            # copy of our array
            temp = res.copy()
            # for all nodes: 
            for sr, ds, pr in flights:
                # if node inf skip
                if res[sr] == float("inf"):
                    continue
                # else check if path to dst is better than current:
                if res[sr] + pr < temp[ds]:  
                    # update the path in the temp array 
                    temp[ds] = res[sr] + pr
            # res = temp 
            res = temp

        # if res[dst]:
        if res[dst] != float("inf"):
            # return res[dst]
            return res[dst]
        # elese: 
        else:
            return -1 
            # -1 



