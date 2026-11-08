class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        optiuni=dict()
        for i,val in enumerate(nums):
            dif=target-val
            if dif in optiuni:
                return [optiuni[dif],i]
            optiuni[val]=i
