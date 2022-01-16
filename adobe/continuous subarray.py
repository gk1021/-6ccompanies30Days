class Solution:
    def subArraySum(self,arr, n, s): 
        i=0
        su1=0
        ini=0
        while i<n:
            su1+=arr[i]
            if su1==s:
                return [ini+1,i+1]
            elif su1>s:
                while su1>s:
                    su1-=arr[ini]
                    ini+=1
                if su1==s:
                    return [ini+1,i+1]
            i+=1
        return [-1]
