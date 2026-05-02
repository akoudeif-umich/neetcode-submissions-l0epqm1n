class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        res = []

        adj = defaultdict(list)

        for course, pre in prerequisites:
            adj[course].append(pre)

        visiting = set()

        visited = set()

        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True
            
            visiting.add(course)

            for n in adj[course]:
                if not dfs(n):
                    return False

            visiting.remove(course)
            visited.add(course)
            res.append(course)
            
            return True
        
        for n in range(numCourses):
            if not dfs(n):
                return []

        return res
            
        

