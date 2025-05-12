# Last updated: 5/11/2025, 9:37:49 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {} 
        for i,n in enumerate(nums):
            m = target - n 
            if m in numDict:
                return [i, numDict[m]]
            else: 
                numDict[n] = i
        
        