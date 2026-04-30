class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = []
        for i in range(numCourses):
            graph.append([])

        for pair in prerequisites:
            course = pair[0]
            prereq = pair[1]
            graph[prereq].append(course)

        state = []
        for i in range(numCourses):
            state.append(0)


        def dfs(course: int) -> bool:
            if state[course] == 1:
                return True

            if state[course] == 2:
                return False

            state[course] = 1
            for neighbour in graph[course]:
                if dfs(neighbour):
                    return True

            state[course] = 2
            return False
        
        for course in range(numCourses):
            if state[course] == 0:
                if dfs(course):
                    return False
        
        return True
    
      
# numCourses = 3
# prereqs = [[1, 0], [2, 1]]
# Graph = 0 -> 1, 1 -> 2
# State = [0, 0, 0]

