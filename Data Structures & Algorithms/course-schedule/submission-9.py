class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        adj = defaultdict(list)

        for course, pre in prerequisites:
            adj[course].append(pre)

        visiting = set()

        
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
            
        
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
