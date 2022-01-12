class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,arr,n,k):
        fs=arr[0]
        i=0
        mv=-1
        li=[]
        while i<n-k+1:
            if fs==mv or mv==-1:
                mv=max(arr[i:i+k])
            else:
                mv=max(mv,arr[i+k-1])
            fs=arr[i]
            li.append(mv)
            
            i+=1
        return li
