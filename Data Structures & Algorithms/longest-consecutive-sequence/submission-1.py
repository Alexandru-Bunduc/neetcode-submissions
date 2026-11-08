class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        result=0
        for i in nums:
            localresult=0
            if i-1 not in nums:
                j=i+1
                while j in nums:
                    j+=1 
                localresult=j-i
                if result<localresult:
                    result=localresult
        return result

                
