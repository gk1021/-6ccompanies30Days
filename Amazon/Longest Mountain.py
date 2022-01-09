class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr)<3:
            return 0
        maxL=0
        
        i=1
        flag=0
        l=0
        while i<len(arr):
            #print(l,maxL,flag,arr[i],arr[i-1])
            if arr[i]>arr[i-1] and flag==0:
                
                l+=1
            elif arr[i]<arr[i-1] and flag==0 and l!=0:
                l+=1
                flag=1
            elif arr[i]<arr[i-1] and flag==1:
                l+=1
            elif arr[i]>arr[i-1] and flag==1:
                if l>maxL and flag==1:
                    maxL=l
                flag=0
                l=1
            else:
                if l>maxL and flag==1:
                    maxL=l
                l=0
                flag=0
                
            #print(l,maxL,flag,arr[i],arr[i-1])
            i+=1
            
        if l>maxL and flag==1:
            maxL=l
        if maxL<=1:
            return 0
        return maxL+1
        
