class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        visiting = set()

        adj = defaultdict(list)

        for course, pre in prerequisites:
            adj[course].append(pre)

        
        def dfs(course):
            if course in visiting:
                return False
            if adj[course] == []:
                return True
            
            visiting.add(course)

            for pre in adj[course]:
                if not dfs(pre):
                    return False

            visiting.remove(course)
            adj[course] = []
            
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True