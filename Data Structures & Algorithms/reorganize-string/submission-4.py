class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        freq = {} # character -> count

        for c in s:
            if c in freq:
                freq[c] = freq[c] + 1
            else:
                freq[c] = 1
        
        max_count = 0
        for c in freq:
            if freq[c] > max_count: 
                max_count = freq[c]
        
        if max_count > (n+1)//2:
            return ""

        heap = []
        for c in freq:
            count = freq[c]

            heapq.heappush_max(heap, (count, c))
        
        result_chars = []

        prev_char = None
        prev_count = 0

        while len(heap) > 0:
            cur_count, cur_char = heapq.heappop_max(heap)
            result_chars.append(cur_char)
            cur_count = cur_count-1

            if prev_char and prev_count > 0:
                heapq.heappush_max(heap, (prev_count, prev_char))

            prev_char = cur_char
            prev_count = cur_count
        
        result = "".join(result_chars)

        if len(result) == n:
            return result
        else:
            return ""

"aab"