class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for x1, y1 in points:
            dist = -(x1 ** 2 + y1 ** 2)
            heapq.heappush(maxHeap, [dist, x1, y1])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        res = []

        while maxHeap:
            dist,x,y = heapq.heappop(maxHeap)
            res.append([x,y])
        return res



