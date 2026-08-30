# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         graph = [[] for _ in range(numCourses)]
#         for course, prereq in prerequisites:
#             graph[course].append(prereq)
#         state = [0] * numCourses

#         def dfs(course):
#             if state[course] == 1:
#                 return False
#             if state[course] == 2:
#                 return True
#             state[course] = 1

#             for prereq in graph[course]:
#                 if not dfs(prereq):
#                     return False
#             state[course] = 2
#             return True

#         for i in range(numCourses):
#             if not dfs(i):
#                 return False
#         return True

        
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        reqs = [0] * numCourses
        adj_list = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            reqs[course] += 1
        print(reqs)
        q = collections.deque()
        for i in range(len(reqs)):
            if reqs[i] == 0:
                q.append(i)
        finish = 0
        while q:
            course = q.popleft()
            for each in adj_list[course]:
                reqs[each] -= 1
                if reqs[each] == 0:
                    q.append(each)
            finish += 1
        print(finish)
        print(reqs)
        return finish == numCourses




