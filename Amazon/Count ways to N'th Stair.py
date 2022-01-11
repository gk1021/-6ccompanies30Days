
class Solution:
    
    #Function to count number of ways to reach the nth stair 
    #when order does not matter.
    def countWays(self,m):
        
        mod = 1000000007
        
        c=m//2+1
        return c%mod
