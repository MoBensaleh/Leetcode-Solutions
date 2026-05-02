class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        write = 0
        read = 1

        while read < len(nums):
            if nums[read] != nums[write]:
                write = write + 1
                nums[write] = nums[read]
            
            read = read+1

        k = write + 1

        return k