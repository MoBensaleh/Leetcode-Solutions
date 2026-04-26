class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i: [] for i in range(n)}

        visit = set()

        for node, neigh in edges:
            adj[node].append(neigh)
            adj[neigh].append(node)
        
        def dfs(node, prev):
            if node in visit:
                return False
            
            visit.add(node)
            for neigh in adj[node]:
                if neigh == prev:
                    continue
                if not dfs(neigh, node):
                    return False
            return True
         
        return dfs(0,-1) and len(visit) == n
        

        


                
            


