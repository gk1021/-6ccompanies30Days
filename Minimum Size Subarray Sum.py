class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        i=0
        n=9999999
        sums=0
        l=0
        #sums.append(nums[i])
        while i<len(nums):
            sums+=nums[i]
            while sums>=target:
                n=min(n,i+1-l)
                sums-=nums[l]
                l+=1
            i+=1
        if n==9999999:
            n=0
        return n
