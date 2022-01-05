class Solution:
    def decodedString(self, s):
        ds=""
        digits=['0','1','2','3','4','5','6','7','8','9']
        li=[]
        top=0
        for i in s:
            if i!=']':
                li.append(i)
                top+=1
            else:
                ele=li.pop(top-1)
                top-=1
                st=""
                while ele!='[':
                    st=ele+st
                    ele=li.pop(top-1)
                    top-=1
                ele1=''
                while top>0 and li[top-1] in digits:
                    ele1=li.pop(top-1)+ele1
                    top-=1
                
                
                st2=st*int(ele1)
                #print(st2)
                li.append(st2)
                top+=1
            #print(li)
        ds=li.pop(top-1)
        top-=1
        n=""
        #print(li)
        while top>0:
            n=n+li.pop(top-1)
            top-=1
        if n:
            ds=int(n)*ds
        return ds
