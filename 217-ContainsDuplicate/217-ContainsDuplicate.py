# Last updated: 5/12/2025, 12:17:17 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums: 
            if n in seen:
                return True
            else:
                seen.add(n)
        return False