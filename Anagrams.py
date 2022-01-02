
class Solution:
    def Anagrams(self, words, n):
        
        dic2={}
        for i in words:
            si=sorted(i)
            si="".join(si)
            if si in list(dic2.keys()):
                dic2[si].append(i)
            else:
                dic2[si]=[i]
                
        return_l=[]
        for k in dic2.keys():
            return_l.append(dic2[k])
        #print(dic2)
        return return_l
