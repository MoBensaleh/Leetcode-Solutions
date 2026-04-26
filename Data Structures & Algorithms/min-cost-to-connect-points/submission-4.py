class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)

        adj = {i:[] for i in range(N)} # [cost, node]
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2,y2 = points[j]
                distance = abs(x1-x2) + abs(y1-y2)
                adj[i].append([distance, j])
                adj[j].append([distance, i])
        
        res=0
        visit=set()
        minHeap = [[0,0]]

        while len(visit) < N:
            cost, point = heapq.heappop(minHeap)
            if point in visit:
                continue
            res+=cost
            visit.add(point)
            for nei_cost, nei_point in adj[point]:
                if nei_point not in visit: 
                    heapq.heappush(minHeap, [nei_cost, nei_point])
        return res