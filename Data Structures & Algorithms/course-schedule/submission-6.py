class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # keep track of nodes currently in dfs 
        visiting = set()

        # build adj list
        courses = defaultdict(list)
        for course, pre in prerequisites:
            courses[course].append(pre)

        # dfs function 
        def dfs(course):
            # if it is in visiting return false
            if course in visiting:
                return False
            # if the course has no prereqs return true
            if courses[course] == []:
                return True

            # mark the node as visiting 
            visiting.add(course)

            # check children nodes, 
            for pre in courses[course]:
            # either you run back into current node or reach a class with no prereq
                if not dfs(pre):
                    return False

            # after each child has been checked the current course has been cleared
            # clear its pre reqs
            courses[course] = []
            # remove it from visiting 
            visiting.remove(course)
        
            return True

        # loop through numCourses and call dfs on each one 
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
        

