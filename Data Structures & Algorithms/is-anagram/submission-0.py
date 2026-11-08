class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frs=dict()
        frt=dict()
        for i in s:
            frs[i]=frs.get(i,0)+1
        for i in t:
            frt[i]=frt.get(i,0)+1
        if frs.keys()!=frt.keys():
            return False
        else:
            for j in frs.keys():
                if frt[j]!=frs[j]:
                    return False
        return True    