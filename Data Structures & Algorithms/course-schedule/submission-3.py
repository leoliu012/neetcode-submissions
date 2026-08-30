class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        state = [0] * numCourses

        def dfs(course):
            if state[course] == 1:
                return False
            if state[course] == 2:
                return True
            state[course] = 1

            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            state[course] = 2
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

        

