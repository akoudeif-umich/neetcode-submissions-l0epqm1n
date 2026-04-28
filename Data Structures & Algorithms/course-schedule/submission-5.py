class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        We want to know if we can take all courses 0 - numCourses - 1

        For each prereq: 
            [course, prereq]
        
        what is the size of prereq list? 
        is it possible to run into a prereq that is > numCourses - 1?
        constraints say:  [course, prereq] < numCourses

        So what makes it impossible to take a course?
        Can a two courses be listed as pre-reqs of eachother?
        EX: [[0, 1], [1, 0]]
        would make it impossible to take these courses 

        Approach:
        dict of seen courses
        Maybe loop through pre-requisites:
            check if the pre-req exists as a key in the map:
                yes then return false
            seen[course] = pre-req (even if a course has multiple pre-reqs we dont need to know about it)
        return True
        Time: O(n)
        space: O(n)

        Approach 2: 
        build out an adj list and use dfs to dect a cycle 

        time: O(v + e)
        space: O(v + e)

        tried approach one but it fails to consider many edge cases
        hard for me to think of edge cases for this problem 
        going to try appoach 2 
        """

        # need a courses dict for adj list
        courses = defaultdict(list)

        # visiting set to keep track of courses we have already checked 
        visiting = set()

        # build out an adj list
        for course, pre in prerequisites:
            courses[course].append(pre)

        def dfs(course):
            # course is currently in the dfs loop 
            if course in visiting:
                return False
            # course has no pre reqs or its pre reqs have been cleared
            if courses[course] == []:
                return True
            
            # add the current course to visited
            visiting.add(course)

            # loop through the current courses pre-reqs
            for pre in courses[course]:
                # if the dfs on the prereq is false then return false
                if not dfs(pre):
                    return False
            # all of current courses pre reqs have been cleared so we dont need to check it anymore
            visiting.remove(course)
            # we have check all the courses prereqs so we can make its list empty
            courses[course] = []

            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True


