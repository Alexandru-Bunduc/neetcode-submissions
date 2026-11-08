class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        result=0
        for i in numSet:
            localresult=0
            if i-1 not in numSet:
                j=i+1
                while j in numSet:
                    j+=1 
                localresult=j-i
                if result<localresult:
                    result=localresult
        return result

                
