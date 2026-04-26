class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseMap = {i:[] for i in range(numCourses)}

        visit, cycle = set(), set()
        result = []

        for crs,pre in prerequisites:
            courseMap[crs].append(pre)

        def dfs(course):

            if course in cycle:
                return False
            if course in visit:
                return True
            
            cycle.add(course)
            for pre in courseMap[course]:
                if not dfs(pre):
                    return False
            cycle.remove(course)
            visit.add(course)
            result.append(course)
            return True
        
        for c in range(numCourses):
            if not dfs(c): return []
        return result


        




