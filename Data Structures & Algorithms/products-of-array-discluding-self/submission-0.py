class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a=[0]*len(nums)
        a[0]=1
        right_to_left=1
        for i in range(1,len(nums)):
            a[i]=a[i-1]*nums[i-1]
        for i in range(len(nums)-1,-1,-1):
            a[i]=a[i]*right_to_left
            right_to_left=right_to_left*nums[i]
        return a

            
