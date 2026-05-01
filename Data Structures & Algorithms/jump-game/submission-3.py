class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_reach = 0

        for i in range(n):
            if i > max_reach:
                return False
        

            jump_reach = i + nums[i]
            if jump_reach > max_reach:
                max_reach = jump_reach
            
            if max_reach >= n-1:
                return True

        if max_reach >= n-1:
            return True
        else: 
            return False
    
# [2,3,1,1,4]
