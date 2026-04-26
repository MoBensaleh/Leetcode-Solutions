class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n+1)]

        for u,v,t in times:
            adj[u].append((v,t))
        
        visit = set()
        t = 0
        minHeap = [(0, k)]

        while minHeap:
            t1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            t = max(t, t1)
            visit.add(n1)

            for nei_node, nei_time in adj[n1]:
                if nei_node not in visit:
                    heapq.heappush(minHeap, [t1 + nei_time, nei_node])
        return t if len(visit) == n else -1