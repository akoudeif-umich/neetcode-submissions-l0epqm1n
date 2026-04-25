class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(list)
        visited = set()

        for course, prereq in prerequisites:
            courses[course].append(prereq)


        def dfs(course):
            if course in visited:
                return False
            if courses[course] == []:
                return True

            visited.add(course)

            for pre in courses[course]:
                if not dfs(pre):
                    return False
            
            visited.remove(course)
            courses[course] = []

            return True

        for c in range(numCourses):
            if not dfs(c): 
                return False
        return True


        
            