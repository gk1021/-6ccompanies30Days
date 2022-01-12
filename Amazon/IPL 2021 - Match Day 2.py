class Solution:
    def max_of_subarrays(self,arr,n,k):
        '''
        you can use collections module here.
        :param a: given array
        :param n: size of array
        :param k: value of k
        :return: A list of required values 
        '''
        #code here
        li=[]
        fs=arr[0]
        mv=-1
        i=0
        while i<n-k+1:
            if fs==mv or mv==-1:
                mv=max(arr[i:i+k])
            else:
                mv=max(mv,arr[i+k-1])
            li.append(mv)
            fs=arr[i]
            i+=1
        return li
