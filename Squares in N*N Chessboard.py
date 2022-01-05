class Solution:
    def squaresInChessBoard(self, N):
        s=0
        for i in range(1,N+1):
            s+=i**2
        return s
