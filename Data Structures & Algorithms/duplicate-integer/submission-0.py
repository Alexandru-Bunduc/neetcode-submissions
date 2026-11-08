class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        fr=dict()
        for i in nums:
            if i in fr:
                return True
            else:
                fr[i]=1
        return False
