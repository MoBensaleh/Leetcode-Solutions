class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        best = {}
        for i in range(len(x)):
            xi = x[i]                
            yi = y[i]                  
            if xi not in best or yi > best[xi]:
                best[xi] = yi      
        if len(best) < 3:
            return -1
        b = sorted(best.values(), reverse=True)
        return b[0] + b[1] + b[2]