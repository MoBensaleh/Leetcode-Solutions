class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)

        maxCount = 0
        res = 0

        for num in nums:
            count[num] += 1

            if maxCount < count[num]:
                maxCount = count[num]
                res = num
        return res
            

        