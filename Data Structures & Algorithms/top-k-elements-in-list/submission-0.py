class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets=[[] for _ in range(len(nums)+1)]
        result=[]
        total=dict()
        for i in nums:
            total[i]=total.get(i,0)+1
        for no,frq in total.items():
            buckets[frq].append(no)
        for i in buckets[::-1]:
            for j in i[::-1]:
             result.append(j)
             if len(result)==k:
                 return result
            

