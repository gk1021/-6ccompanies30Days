class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if len(str1)<len(str2):
            st=str1
        else:
            st=str2
        
        i=len(st)
        while i>0:
            ct=st[:i]
            if ct*(len(str1)//len(ct))==str1 and ct*(len(str2)//len(ct))==str2:
                return ct
            else:
                i-=1
        return ""
