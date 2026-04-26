class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        course_prereq_map = {i:[] for i in range(numCourses)}
        visited = set()

        for crs,pre in prerequisites:
            course_prereq_map[crs].append(pre)
        

        def dfs(course):
            if course in visited:
                return False
            if course_prereq_map[course] == []:
                return True
            
            visited.add(course)
            for pre in course_prereq_map[course]:
                if not dfs(pre): return False
            visited.remove(course)
            course_prereq_map[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c): return False
        return True

        