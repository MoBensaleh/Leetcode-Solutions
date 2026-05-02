class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        max_area = 0

        while left < right:
            width = right - left

            if heights[left] < heights[right]:
                container_height = heights[left]
            else:
                container_height = heights[right]
            
            current_area = width * container_height

            if current_area > max_area:
                max_area = current_area
            
            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
            
        return max_area
    