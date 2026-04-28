class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            curr_value = nums[i]
            complement = target - curr_value

            if complement in seen:
                return [seen[complement], i]
            
            seen[curr_value] = i
        return [-1, -1]