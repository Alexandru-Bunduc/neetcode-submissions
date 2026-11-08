class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        total=dict()
        for string in strs:
            frq=[0]*26
            for letter in string:
                frq[ord(letter)-ord('a')]+=1
            frtuplu=tuple(frq)
            if frtuplu not in total:
                total[frtuplu]=[]
            total[frtuplu].append(string)
        result=list()
        for i in total:
             result.append(total[i])  
        return result
              

