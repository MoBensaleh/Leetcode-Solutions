class Solution:
    def maxSubArray(self, nums):
        # Initialize max_sum to the smallest possible integer
        max_sum = float('-inf')
        # Initialize current_sum to 0
        current_sum = 0
        
        # Iterate over each number in the array
        for num in nums:
            # Add the current number to current_sum
            current_sum += num
            # Update max_sum if current_sum is greater
            max_sum = max(max_sum, current_sum)
            # Reset current_sum to 0 if it becomes negative
            if current_sum < 0:
                current_sum = 0
        
        # Return the maximum sum found
        return max_sum