def isP(p):
        i=0
        f=1
        while i<8:
            if p[i]!=0 and p[i] in p[i+1:]:
                f=0
            i+=1
        return f
class Solution:
    
    
    def isValid(self, mat):
        flag=1
        for i in mat:
            if isP(i)==0:
                return 0
        i=0
        while i<9:
            p=[]
            for j in mat:
                p.append(j[i])
            if isP(p)==0:
                return 0
            i+=1
            
        count=1
        i=0
        while i<9:
            j=0
            
            while j<9:
                p=[]
                p.extend(mat[i][j:j+3])
                p.extend(mat[i+1][j:j+3])
                p.extend(mat[i+2][j:j+3])
                if isP(p)==0:
                    return 0
            
                j+=3
            j=0
            i+=3
        return 1
        
