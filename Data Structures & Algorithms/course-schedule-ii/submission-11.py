class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # prereqs = [set() for _ in range(numCourses)]
        # for prereq in prerequisites:
        #     course = prereq[0]
        #     reqs = prereq[1:]
        #     prereqs[course].add(*reqs)
        
        # q = deque([])
        # added = set()
        # plan = []
        # for i in range(len(prereqs)):
        #     if not prereqs[i]:
        #         q.append(i)
        #         added.add(i)

        # while q:
        #     course = q.popleft()
        #     plan.append(course)
        #     for i in range(len(prereqs)):
        #         prereq = prereqs[i]
        #         if course in prereq:
        #             prereq.remove(course)
        #         if not prereq and i not in added:
        #             added.add(i)
        #             q.append(i)
        #         if len(plan) == numCourses:
        #             return plan
        # return plan if len(plan) == numCourses else []

        affect_list = [[] for _ in range(numCourses)]
        prereqs_left = [0] * numCourses
        for prereq in prerequisites:
            course = prereq[0]
            req = prereq[1]
            affect_list[req].append(course)
            prereqs_left[course] += 1

        q = deque([])
        plan = []
        for course in range(len(prereqs_left)):
            if prereqs_left[course] == 0:
                q.append(course)
        
        while q:
            course = q.popleft()
            plan.append(course)
            new_available = affect_list[course]
            for each in new_available:
                prereqs_left[each] -= 1
                if prereqs_left[each] == 0:
                    q.append(each)

        return plan if len(plan) == numCourses else []
            