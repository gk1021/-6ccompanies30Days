class Solution:
    
    def doOverlap(self, L1, R1, L2, R2):
        hf=0
        wf=0
        h1=[R1[1],L1[1]]
        h2=[R2[1],L2[1]]
        w1=[L1[0],R1[0]]
        w2=[L2[0],R2[0]]
        if (h1[0]>=h2[0] and h1[0]<=h2[1]) or (h1[1]>=h2[0] and h1[1]<=h2[1]) or (h2[0]>=h1[0] and h2[0]<=h1[1]) or (h2[1]>=h1[0] and h2[1]<=h1[1]) :
            hf=1
        if (w1[0]>=w2[0] and w1[0]<=w2[1]) or (w1[1]>=w2[0] and w1[1]<=w2[1]) or (w2[0]>=w1[0] and w2[0]<=w1[1]) or (w2[1]>=w1[0] and w2[1]<=w1[1]) :
            wf=1
        if hf and wf:
            return 1
        return 0
