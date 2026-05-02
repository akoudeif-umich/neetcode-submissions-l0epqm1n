class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Input:
        numCourses >= 1
        [course, pre]

        numCourses = 6
        [0, 1]

        prerequisites:
        [[5, 1], [5, 0], [5, 3], [5, 4], [0, 5]]

        Cycles: make this impossible 

        adj list of courses : [prerequisites]

        loop through graph using dfs 

        if you run into a node you've already seen on the current path
        you hit a cycle so return 

        then you can append to res list 

        """

        # res list
        res = []

        # adj list
        adj = defaultdict(list)
        for course, pre in prerequisites:
            adj[course].append(pre)

        # visiting set
        visiting = set()

        # vistited set
        visited = set()

        # def dfs(course):
        def dfs(course):
            # base cases
            # if in visiting: 
            if course in visiting:
                # return False
                return False
            # if in visited:
            if course in visited:
                return True
                # return True

            # add current course to visiting
            visiting.add(course)

            # loop through neighbors
            for nei in adj[course]:
                # if not dfs(nei):
                if not dfs(nei):
                    return False
                    # return False
                
            # remove from visiting
            visiting.remove(course)
            # add to visited 
            visited.add(course)
            # append to res list
            res.append(course)

            # True
            return True

        # loop through numCourses:
        for course in range(numCourses):
            # if not dfs(course):
            if not dfs(course):
                # return []
                return []
        
        # return res 
        return res










