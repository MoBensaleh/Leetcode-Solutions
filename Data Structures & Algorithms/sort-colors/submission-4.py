class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_zeros = 0
        count_ones = 0
        count_twos = 0

        for v in nums:
            if v == 0:
                count_zeros += 1
            elif v == 1:
                count_ones += 1
            else:
                count_twos += 1
        
        write_idx = 0
        
        for _ in range(count_zeros):
            nums[write_idx] = 0
            write_idx += 1

        for _ in range(count_ones):
            nums[write_idx] = 1 
            write_idx += 1
        
        for _ in range(count_twos):
            nums[write_idx] = 2
            write_idx += 1
        
        return nums