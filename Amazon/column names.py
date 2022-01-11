class Solution:
    def colName (self, n):
        # your code here
        v=""
        n-=1
        while n>=0:
            v=chr(n%26+65)+v
            n=n//26
            n-=1
        return(v)
