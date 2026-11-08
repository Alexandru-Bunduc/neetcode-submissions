class Solution:

    def encode(self, strs: List[str]) -> str:
        enc=""
        for string in strs:
            enc=enc+str(len(string))+"#"+string
        return enc


    def decode(self, s: str) -> List[str]:
        total=[]
        i=0
        while i<len(s):
         j=i+1
         while s[j]!='#':
            j+=1
         lg = int(s[i:j])
         total.append(s[j+1:j+1+lg])
         i=j+1+lg
        return total

        


